"""Checks if installed packages are import-able."""

packages = [
    'numpy',
    'scipy',
    'matplotlib',
    'pandas',
    'seaborn',
    'sklearn',
    'torch',
    'torchvision',
    'tqdm',
    'tensorboard',
    'tensorboardX',
    'PIL',
]

for package in packages:
    try:
        __import__(package)
    except ImportError:
        print(f'{package} is not installed.')
        exit(1)

exit("All packages are installed!")