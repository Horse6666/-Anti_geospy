import argparse
from geospy_defender.protection import load_image, cw_attack, save_image
import torchvision.models as models
from torchvision.models import ResNet50_Weights

def main():
    parser = argparse.ArgumentParser(description="Geospy Defender")
    parser.add_argument("--image", type=str, required=True, help="Path to the input image")
    parser.add_argument("--output", type=str, required=True, help="Path to save the perturbed image")
    parser.add_argument("--c", type=float, default=1e-4, help="Trade-off constant for C&W attack")
    parser.add_argument("--kappa", type=float, default=0, help="Confidence for C&W attack")
    parser.add_argument("--steps", type=int, default=1000, help="Number of steps for C&W attack")
    parser.add_argument("--lr", type=float, default=0.01, help="Learning rate for C&W attack")
    
    args = parser.parse_args()
    
    model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1).eval()
    img_tensor = load_image(args.image)
    perturbed_image = cw_attack(model, img_tensor, c=args.c, kappa=args.kappa, steps=args.steps, lr=args.lr)
    save_image(perturbed_image, args.output)
    
    print(f"Perturbed image saved to {args.output}")

if __name__ == "__main__":
    main()

