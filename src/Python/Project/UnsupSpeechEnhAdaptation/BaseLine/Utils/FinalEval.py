import argparse
import torch
import numpy as np
from tqdm import tqdm
from pprint import pprint
import pickle
import os
import BaseLine.Utils.MixtureConsistency as MixtureConsistency
import BaseLine.Models.ImprovedSudormrf as ImprovedSudormrf
import BaseLine.Metrics.DNNMosMetric as DNNMosMetric
import BaseLine.DatasetLoaders.Chime as Chime
def get_args():
    """! Command line parser"""
    parser = argparse.ArgumentParser(description = "Final evaluation Argument Parser")
    parser.add_argument(
        "--model_checkpoint", type = str,
        help = """The absolute path of a pre-trained separation model that will be used for warm start for the teacher network.""",
        default = None,
    )
    parser.add_argument(
        "--save_results_dir",
        type = str,
        help = """The absolute path for saving the full eval results file.""",
        default = None,
    )
    parser.add_argument(
        "--dataset_split",
        type = str,
        help = """The dataset split name for the CHiME data.""",
        default = 'eval',
        choices = ['eval', 'dev']
    )
    parser.add_argument(
        "--normalize_with_max_absolute_value",
        action="store_true",
        help = """Whether to normalize all audio files to [-1, 1] range.""",
        default=False,
    )
    parser.add_argument(
        "--evaluate_only_input_mixture",
        action = "store_true",
        help = """Whether to use the input mixture instead of a .""",
        default = False,
    )
    return parser.parse_args()
def get_chime_generator(dataset_split):
    data_loader = Chime.Dataset(
        sample_rate = 16000, fixed_n_sources = 1, timelength=-1., augment = False, use_vad = False, zero_pad = False, split = dataset_split, get_only_active_speakers = False,
        normalize_audio = False, n_samples = -1)
    return data_loader.get_generator(batch_size=1, num_workers=1)
def load_sudo_rm_rf_model(path):
    model = ImprovedSudormrf.SuDORMRF( out_channels = 256, in_channels = 512, num_blocks = 8, upsampling_depth = 7, enc_kernel_size = 81, enc_num_basis = 512, num_sources = 2,)
    #You can load the state_dict as here:
    model.load_state_dict(torch.load(path))
    print(f"Fetched model from: {path}")
    return model
if __name__ == "__main__":
    args = get_args()
    hparams = vars(args)
    test_generator = get_chime_generator(hparams['dataset_split'])
    if not hparams["evaluate_only_input_mixture"]:
        model = load_sudo_rm_rf_model(hparams['model_checkpoint'])
        model = model.cuda()
        model.eval()
    else:
        model = None
    test_tqdm_gen = tqdm(enumerate(test_generator), desc='Eval on 16kHz chime 1 speaker')
    res_dic = {"sig_mos": [], "bak_mos": [], "ovr_mos": [],}
    gen_len = len(test_generator)
    with torch.no_grad():
        for j, mixture in test_tqdm_gen:
            np_mixture_mean = mixture[0].cpu().numpy().mean(-1)
            np_mixture_std = mixture[0].cpu().numpy().std(-1)
            if hparams["evaluate_only_input_mixture"]:
                s_est_speech = mixture[0].cpu().numpy()
            else:
                file_length = mixture.shape[-1]
                min_k = int(np.ceil(np.log2(file_length/16000)))
                padded_length = 2**max(min_k, 1) * 16000
                input_mix = torch.zeros((1, padded_length), dtype=mixture.dtype)
                input_mix[..., :file_length] = mixture
                input_mix = input_mix.unsqueeze(1).cuda()
                input_mix_std = input_mix.std(-1, keepdim=True)
                input_mix_mean = input_mix.mean(-1, keepdim=True)
                input_mix = (input_mix - input_mix_mean) / (input_mix_std + 1e-9)
                student_estimates = model(input_mix)
                student_estimates = MixtureConsistency.apply(student_estimates, input_mix)
                s_est_speech = student_estimates[0, 0, :file_length].detach().cpu().numpy()
            if hparams["normalize_with_max_absolute_value"]:
                s_est_speech -= s_est_speech.mean(-1)
                s_est_speech /= np.abs(s_est_speech).max(-1) + 1e-9
            else:
                s_est_speech = (s_est_speech - s_est_speech.mean(-1)) / (s_est_speech.std(-1) + 1e-9)
                s_est_speech = (s_est_speech * np_mixture_std) + np_mixture_mean
            dnsmos_res_dic = DNNMosMetric.compute_dnsmos(s_est_speech, fs=16000)
            for k, v in dnsmos_res_dic.items():
                res_dic[k].append(v)
            ovrl_mos_avg = round(np.mean(res_dic["ovr_mos"]), 2)
            bak_mos_avg = round(np.mean(res_dic["bak_mos"]), 2)
            sig_mos_avg = round(np.mean(res_dic["sig_mos"]), 2)
            test_tqdm_gen.set_description(f"Avg OVRL MOS: {ovrl_mos_avg}, BAK: {bak_mos_avg}, SIG: {sig_mos_avg} {j}/{gen_len}")
    aggregate_results = {}
    for k, values in res_dic.items():
        mean_metric = np.mean(values)
        median_metric = np.median(values)
        std_metric = np.std(values)
        aggregate_results[k] = {'mean': mean_metric, 'median': median_metric, 'std': std_metric}
    pprint(aggregate_results)
    if hparams["evaluate_only_input_mixture"]:
        model_name = 'unprocessed'
    else:
        model_name = os.path.basename(hparams['model_checkpoint'])
    if hparams['save_results_dir'] is None:
        save_path = os.path.join('/tmp', model_name + f'_full_eval_results_{hparams["dataset_split"]}.pkl')
    else:
        save_path = os.path.join(hparams['save_results_dir'], model_name + f'_full_eval_results_{hparams["dataset_split"]}.pkl')

    with open(save_path, 'wb') as handle:
        pickle.dump(aggregate_results, handle, protocol=pickle.HIGHEST_PROTOCOL)