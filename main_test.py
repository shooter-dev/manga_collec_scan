import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QScreen

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test DPI")
        self.setGeometry(100, 100, 400, 300)

        # Obtenir l'instance de l'écran
        screen = QApplication.primaryScreen()
        dpi = screen.logicalDotsPerInch()  # DPI de l'écran
        print(f"DPI de l'écran : {dpi}")

        # Vous pouvez ajuster la mise à l'échelle en fonction du DPI
        # Cela permet de redimensionner les éléments de l'interface si nécessaire
        scale_factor = dpi / 96  # 96 DPI est la référence de base
        print(f"Facteur de mise à l'échelle : {scale_factor}")

        self.setStyleSheet(f"font-size: {scale_factor * 12}pt;")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
