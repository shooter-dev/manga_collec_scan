import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test DPI avec Mise à l'échelle")
        self.setGeometry(100, 100, 800, 480)

        # Ajouter un label pour afficher un texte
        self.label = QLabel(self)
        self.label.setText("Ceci est un test du DPI et du facteur de mise à l'échelle.")
        self.label.setGeometry(50, 100, 300, 50)  # Positionner le label dans la fenêtre

        # Obtenir l'instance de l'écran et le DPI
        screen = QApplication.primaryScreen()
        dpi = screen.logicalDotsPerInch()  # DPI de l'écran
        scale_factor = dpi / 96  # Calcul du facteur de mise à l'échelle

        print(f"DPI de l'écran : {dpi}")
        print(f"Facteur de mise à l'échelle : {scale_factor}")

        # Appliquer le facteur de mise à l'échelle à la taille de police du label
        font = QFont()
        font.setPointSizeF(scale_factor * 10)  # Ajuster la taille de la police selon le DPI
        self.label.setFont(font)  # Appliquer la police mise à l'échelle au label

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
