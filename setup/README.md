
```bash
conda create -n dl2021-cpu
conda activate dl2021-cpu
conda install python=3.9
pip install torch torchvision
pip install pytorch-lightning
pip install tensorboard
pip install tabulate tqdm pillow
conda install scipy scikit-learn matplotlib seaborn pandas
```

> Note: Could not install `torchaudio` and `torchtext` on Mac M1.