import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
import brightness


class BrightnessControlApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Contrôle de la Luminosité')
        self.setGeometry(100, 100, 300, 100)

        # Initialisation de l'interface
        self.layout = QVBoxLayout()

        # Label pour afficher la luminosité actuelle
        self.label = QLabel(f'Luminosité : {brightness.get_brightness() * 100:.0f}%', self)
        self.layout.addWidget(self.label)

        # Slider pour ajuster la luminosité
        self.slider = QSlider()
        self.slider.setOrientation(1)  # Orientation verticale
        self.slider.setRange(0, 100)  # Plage de 0 à 100%
        self.slider.setValue(brightness.get_brightness() * 100)  # Valeur initiale de la luminosité
        self.slider.valueChanged.connect(self.update_brightness)
        self.layout.addWidget(self.slider)

        # Mettre en place la mise en page
        self.setLayout(self.layout)

    def update_brightness(self):
        # Mise à jour de la luminosité
        brightness.set_brightness(self.slider.value() / 100)
        self.label.setText(f'Luminosité : {self.slider.value()}%')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BrightnessControlApp()
    window.show()
    sys.exit(app.exec_())
