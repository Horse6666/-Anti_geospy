import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
from geospy_defender.protection import load_image, cw_attack, save_image
import torchvision.models as models

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Geospy Defender'
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 800, 600)
        
        layout = QVBoxLayout()
        
        self.label = QLabel(self)
        self.label.setText("Select an image to protect:")
        layout.addWidget(self.label)
        
        self.btn = QPushButton('Open Image', self)
        self.btn.clicked.connect(self.open_image)
        layout.addWidget(self.btn)
        
        self.setLayout(layout)
        
    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.jpeg)", options=options)
        if file_name:
            model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1).eval()
            img_tensor = load_image(file_name)
            perturbed_image = cw_attack(model, img_tensor)
            save_image(perturbed_image, "perturbed_image.jpg")
            pixmap = QPixmap("perturbed_image.jpg")
            self.label.setPixmap(pixmap)
            self.label.resize(pixmap.width(), pixmap.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
