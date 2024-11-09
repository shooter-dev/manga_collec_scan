import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Affichage exact de 10 pixels")
        self.setGeometry(1, 1, 1280, 720)

        # Créer un label pour afficher un carré de 10x10 pixels
        label = QLabel(self)
        label.setText("10x10 pixels")
        label.setStyleSheet("background-color: red;")
        label.setGeometry(1, 1, 1278, 718)  # Spécifiez la taille exacte en pixels

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Empêcher l'adaptation automatique de la mise à l'échelle pour les éléments graphiques
    app.setAttribute(Qt.AA_EnableHighDpiScaling, False)

    window = MyWindow()
    sys.exit(app.exec_())
