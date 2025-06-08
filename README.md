# MobileNetV2 Deployment on Kria KV260 using Vitis AI

This project demonstrates the end-to-end deployment of a MobileNetV2 model on the Kria KV260 board using the Vitis AI toolchain.

## 🛠 Prerequisites

- Ubuntu 20.04 with Xilinx tools installed
- Python 3.8+
- Vitis AI Docker or native install
- PyTorch
- torchvision
- Vitis AI tools (quantizer, compiler)

## 🧪 Step 1: Train and Save Model

```python
from torchvision import models
import torch.nn as nn
import torch

model = models.mobilenet_v2(pretrained=True)
model.classifier[1] = nn.Linear(model.last_channel, 80)  # Adjust classes
torch.save(model.state_dict(), 'model/model.pth')
```
## 🔍 Step 2: Quantization
bash
Copy
Edit
python quantize.py
Quantizes the model and generates files like:

quantized/quant_info.json

quantized/MobileNetV2.py

