import torch
import matplotlib.pyplot as plt

from device.Device import get_default_device, to_device

from dataset.data_prepation import dataset, transformations

from modelArchitecture import ResNet

device = get_default_device()


model = ResNet()

model.load_state_dict(torch.load('modelparam.pth',  weights_only=True))
model = to_device(model,device)
model.eval()  


def predict_image(img, model):
    # Convert to a batch of 1
    xb = to_device(img.unsqueeze(0), device)
    # Get predictions from model
    yb = model(xb)
    # Pick index with highest probability
    prob, preds  = torch.max(yb, dim=1)
    # Retrieve the class label
    return dataset.classes[preds[0].item()]


from PIL import Image
from pathlib import Path

def predict_external_image(image_name):
    image = Image.open(Path('./' + image_name))

    example_image = transformations(image)
    plt.imshow(example_image.permute(1, 2, 0))
    print("The image resembles", predict_image(example_image,model) + ".")