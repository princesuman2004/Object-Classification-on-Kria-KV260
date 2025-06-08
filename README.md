# MobileNetV2 Deployment on Kria KV260 using Vitis AI

This project demonstrates the end-to-end deployment of a MobileNetV2 model on the Kria KV260 board using the Vitis AI toolchain.

##  Prerequisites

- Ubuntu 20.04 with Xilinx tools installed
- Python 3.8+
- Vitis AI Docker or native install
- PyTorch
- torchvision
- Vitis AI tools (quantizer, compiler)

##  Step 1: Train and Save Model

```python
from torchvision import models
import torch.nn as nn
import torch

model = models.mobilenet_v2(pretrained=True)
model.classifier[1] = nn.Linear(model.last_channel, 80)  # Adjust classes
torch.save(model.state_dict(), 'model/model.pth')
```

##  Step 2: Quantization

```bash
python quantize.py
```

Quantizes the model and generates files like:
- `quantized/quant_info.json`
- `quantized/MobileNetV2.py`

##  Step 3: Export the Quantized Model

Export the .xmodel required for the compiler:

```bash
python export_xmodel.py
```

Generates:
- `quantize_result/MobileNetV2_int.xmodel`

##  Step 4: Compile for KV260

Use the Vitis AI compiler (vai_c_xir) to target the KV260 board:

```bash
vai_c_xir \
  --xmodel quantize_result/MobileNetV2_int.xmodel \
  --arch /opt/vitis_ai/compiler/arch/DPUCZDX8G/KV260/arch.json \
  --output_dir compiled_model \
  --net_name mobilenetv2_kv260
```

Output:
- `compiled_model/mobilenetv2_kv260.xmodel`
- `compiled_model/meta.json`

##  Output Summary

- **Compiled model**: in `compiled_model/` ready for DPU
- **Quantization artifacts**: in `quantized/`
- **Exported .xmodel**: in `quantize_result/`

## 📃 License

MIT License
