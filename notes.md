## Tutorial 2: Introduction to PyTorch

### Questions

1. Is dataloader shuffled after every epoch?
2. Should we apply transforms in `__getitem__` or during the forward pass? Specific cases: contrastive learning or mixup augmentation!
3. Where should we transport data onto GPU, ideally?
   1. After loading batches during the training loop!