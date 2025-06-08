import torch
import torch.nn as nn
from torchvision.models import mobilenet_v2
from pytorch_nndct.apis import torch_quantizer

# Step 1: Define model structure
model = mobilenet_v2(pretrained=False)
model.classifier[1] = nn.Linear(model.last_channel, 80)
model.eval()

# Step 2: Create dummy input
dummy_input = torch.randn(1, 3, 224, 224)

# Step 3: Create quantizer in 'test' mode without specifying quant_config_file
quantizer = torch_quantizer(
    quant_mode='test',
    module=model,
    input_args=(dummy_input,),
    output_dir='quantized',
    device=torch.device('cpu')
)

# Step 4: Perform a forward pass
quant_model = quantizer.quant_model
quant_model(dummy_input)

# Step 5: Export the .xmodel
quantizer.export_xmodel()
print("deploy_model.xmodel successfully exported to quantized/")
