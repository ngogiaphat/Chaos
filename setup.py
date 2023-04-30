from setuptools import setup
setup(
    name = 'Chaos',
    version = '',
    package = [''],
    package_dir = {'': 'src'},
    url = 'https://github.com/ngogiaphat',
    keywords='development, setup, setuptools',
    python_requires='>=3.7, <4',
    license = '',
    author = 'me',
    author_email = 'ngogiaphat0802@gmail.com',
    description = '',
    classifiers = [
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3',
    ],
    install_requires = [
        'PyYAML',
        'pandas == 0.23.3',
        'numpy >=1.14.5',

        'jupyter'
    ],
    package_data = {
        'sample': ['sample_data.csv'],
    },
    entry_points = {
        'runners': [
            'sample=sample:main',
        ]     
    }
)