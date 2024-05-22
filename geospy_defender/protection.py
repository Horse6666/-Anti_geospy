import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import torchattacks

def load_image(image_path):
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    img = Image.open(image_path)
    img_tensor = preprocess(img).unsqueeze(0)
    return img_tensor

def cw_attack(model, img_tensor, c=1e-4, kappa=0, steps=1000, lr=0.01):
    attack = torchattacks.CW(model, c=c, kappa=kappa, steps=steps, lr=lr)
    perturbed_image = attack(img_tensor, torch.tensor([model(img_tensor).argmax()]))
    return perturbed_image

def save_image(tensor, path):
    img = transforms.ToPILImage()(tensor.squeeze())
    img.save(path)



