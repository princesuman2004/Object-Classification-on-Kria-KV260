import torch
import torch.nn as nn
from pytorch_nndct import torch_quantizer
import torchvision.models as models
import os, cv2, numpy as np

# Define model (MobileNetV2)
model = models.mobilenet_v2(pretrained=False)
model.classifier[1] = nn.Linear(model.classifier[1].in_features, 80)

# Load trained weights
model.load_state_dict(torch.load("model/model.pth", map_location=torch.device("cpu")))
model.to("cpu")
model.eval()

# Preprocessing
def preprocess(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32) / 255.0
    img = (img - 0.5) / 0.5
    img = np.transpose(img, (2, 0, 1))
    return torch.tensor(img).unsqueeze(0)

# Calibration loader
def calib_loader():
    for root, _, files in os.walk("calibration_images"):
        for f in files:
            if f.lower().endswith((".jpg", ".png")):
                yield preprocess(os.path.join(root, f))

# Quantization
quantizer = torch_quantizer("calib", model, (next(calib_loader()),), output_dir="quantized")
quant_model = quantizer.quant_model

for i, img in enumerate(calib_loader()):
    if i >= 50: break
    quant_model(img)

quantizer.export_quant_config()
print(" Quantization complete")
