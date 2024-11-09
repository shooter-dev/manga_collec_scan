import os
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Définir le facteur de mise à l'échelle en fonction de votre calcul
scale_factor = 0.345
os.environ["QT_SCALE_FACTOR"] = str(scale_factor)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulation de l'écran cible avec QT_SCALE_FACTOR")
        self.resize(720, 1280)  # Taille logique cible

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
