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

        # Essayer de récupérer la luminosité actuelle
        try:
            current_brightness = brightness.get_brightness()  # Luminosité en pourcentage
        except Exception as e:
            current_brightness = 50  # Valeur par défaut si l'appel échoue
            print(f"Erreur lors de la récupération de la luminosité : {e}")

        # Label pour afficher la luminosité actuelle
        self.label = QLabel(f'Luminosité : {current_brightness}%', self)
        self.layout.addWidget(self.label)

        # Slider pour ajuster la luminosité
        self.slider = QSlider()
        self.slider.setOrientation(1)  # Orientation verticale
        self.slider.setRange(0, 100)  # Plage de 0 à 100%
        self.slider.setValue(current_brightness)  # Valeur initiale de la luminosité
        self.slider.valueChanged.connect(self.update_brightness)
        self.layout.addWidget(self.slider)

        # Mettre en place la mise en page
        self.setLayout(self.layout)

    def update_brightness(self):
        # Mise à jour de la luminosité
        brightness.set(self.slider.value())  # Mettre la luminosité à la valeur du slider
        self.label.setText(f'Luminosité : {self.slider.value()}%')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BrightnessControlApp()
    window.show()
    sys.exit(app.exec_())
