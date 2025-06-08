# MobileNetV2 Deployment on Kria KV260

This repository contains a complete implementation for quantizing, compiling, and deploying a MobileNetV2 model on the AMD Kria KV260 FPGA board using Vitis AI.

## Project Structure

```
├── calibration_images/     # Calibration dataset for quantization
├── compiled_model/         # Final compiled model for KV260 deployment
├── model/                  # Original trained model files
├── quantize_result/        # Exported .xmodel files
├── quantized/             # Quantization artifacts and intermediate files
├── export_xmodel.py       # Script to export quantized model to .xmodel format
├── quantize.py            # Model quantization script
└── README.md              # This file
```

## Overview

This project demonstrates the complete workflow for deploying a custom MobileNetV2 model on the Kria KV260 board. The model is trained with 80 output classes and goes through quantization, export, and compilation stages to be compatible with the DPU (Deep Processing Unit) on the KV260.

## Prerequisites

- Vitis AI development environment
- PyTorch with torchvision
- Kria KV260 board with appropriate setup
- Calibration dataset for quantization

## Deployment Workflow

### Step 1: Model Training and Saving

The MobileNetV2 model is trained using torchvision with a custom classifier for 80 classes:

```python
model = models.mobilenet_v2(pretrained=True)
model.classifier[1] = nn.Linear(model.last_channel, 80)
torch.save(model.state_dict(), 'model/model.pth')
```

**Generated Files:**
- `model/model.pth` - Trained model state dictionary

### Step 2: Model Quantization

The trained model is quantized using the Vitis AI quantizer with calibration mode:

```python
quantizer = torch_quantizer(
    quant_mode='calib',
    module=model,
    input_args=(dummy_input,),
    output_dir='quantized',
    device=torch.device('cpu')
)
```

**Generated Files:**
- `quantized/quant_info.json` - Quantization configuration
- `quantized/bias_corr.pth` - Bias correction parameters
- `quantized/MobileNetV2.py` - Quantized model definition

### Step 3: Export to .xmodel Format

The quantized model is exported to Vitis AI's .xmodel format using test mode:

```python
quantizer = torch_quantizer(
    quant_mode='test',
    module=model,
    input_args=(dummy_input,),
    output_dir='quantized',
    device=torch.device('cpu')
)
quant_model = quantizer.quant_model
quant_model(dummy_input)
quantizer.export_xmodel()
```

**Generated Files:**
- `quantize_result/MobileNetV2_int.xmodel` - Exported model in .xmodel format

### Step 4: Compilation for KV260

The .xmodel is compiled using VAI_C compiler targeting the KV260 architecture:

```bash
vai_c_xir \
    --xmodel quantize_result/MobileNetV2_int.xmodel \
    --arch /opt/vitis_ai/compiler/arch/DPUCZDX8G/KV260/arch.json \
    --output_dir compiled_model \
    --net_name mobilenetv2_kv260
```

**Generated Files:**
- `compiled_model/mobilenetv2_kv260.xmodel` - Final compiled model for deployment
- `compiled_model/meta.json` - Compilation metadata

## Usage Instructions

1. **Setup Environment**: Ensure Vitis AI development environment is properly configured

2. **Prepare Calibration Data**: Place representative images in the `calibration_images/` folder for quantization calibration

3. **Run Quantization**: Execute the quantization script
   ```bash
   python quantize.py
   ```

4. **Export Model**: Convert to .xmodel format
   ```bash
   python export_xmodel.py
   ```

5. **Compile for KV260**: Use the VAI_C compiler as shown in Step 4

6. **Deploy**: Transfer the compiled model to your KV260 board and integrate with your inference application

## Important Notes

- All steps must be completed in sequence for compatibility with the Vitis AI toolchain
- The model is configured for 80 output classes - modify the classifier layer if different number of classes is needed
- Calibration data should be representative of your target inference data for optimal quantization results
- The compiled model is specifically targeted for the KV260 board's DPU architecture

## File Dependencies

- `quantize.py` depends on the trained model in `model/model.pth`
- `export_xmodel.py` depends on quantization results from the `quantized/` folder
- VAI_C compilation depends on the exported .xmodel from `quantize_result/`

## Troubleshooting

- Ensure all file paths are correctly specified in the scripts
- Verify that the Vitis AI environment variables are properly set
- Check that the calibration dataset contains sufficient representative samples
- Confirm the KV260 board architecture file is available at the specified path

## Hardware Requirements

- AMD Kria KV260 Vision AI Starter Kit
- Sufficient host machine resources for model training and quantization
- Network connection for model transfer to the board
