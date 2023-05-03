import torch
def apply(pr_batch, input_mixture, mix_weights_type = "uniform"):
    """
    :param pr_batch: Torch Tensors of size: batch_size x self.n_sources x length_of_wavs
    :param input_mixture: Torch Tensors of size: batch_size x 1 x length_of_wavs
    :param mix_weights_type: type of wights applied
    """
    num_sources = pr_batch.shape[1]
    pr_mixture = torch.sum(pr_batch, keepdim = True)
    if mix_weights_type == "magsq":
        mix_weights = torch.mean(pr_mixture) / num_sources