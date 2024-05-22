# Geospy Defender

Geospy Defender is a tool designed to protect your images from being identified by geolocation recognition systems like Geospy. By adding adversarial noise to your images, Geospy Defender ensures your privacy.

## Installation

```bash
git clone https://github.com/Horse6666/geospy_defender.git
cd geospy_defender
pip install -r requirements.txt
pip install torchattacks
```

# Usage
## Command Line Interface
You can use the command line interface to generate adversarial images. Run the following command, specifying the path to the input image, the path to save the perturbed image, and the parameters for the adversarial noise generation:
```bash
python -m geospy_defender --image path/to/image.jpg --output path/to/perturbed_image.jpg --c 1e-4 --kappa 0 --steps 1000 --lr 0.01
```
## Parameters
`--image`: Path to the input image.
`--output`: Path to save the perturbed image.
`--c`: Trade-off constant for C&W attack, controls the magnitude of adversarial noise.
`--kappa`: Confidence parameter for C&W attack, higher values make the attack more noticeable but stronger.
`--steps`: Number of steps for the optimization process.
`--lr`: Learning rate for the optimization process.



## Graphical User Interface
You can also use the graphical user interface to interactively select and process images. Run the following command to start the GUI:
```bash
python app/app.py
```