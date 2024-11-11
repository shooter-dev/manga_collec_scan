from PyQt5.QtWidgets import QApplication, QComboBox, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QEvent, QPoint
import sys

class SwipeComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_AcceptTouchEvents)
        self.start_pos = None  # Pour stocker la position de départ du glissement

    def touchEvent(self, event):
        if event.type() == QEvent.TouchBegin:
            # Enregistrer la position de départ du glissement
            self.start_pos = event.touchPoints()[0].pos()
        elif event.type() == QEvent.TouchEnd and self.start_pos is not None:
            # Obtenir la position de fin du glissement
            end_pos = event.touchPoints()[0].pos()
            self.handleSwipe(end_pos)
        return super().touchEvent(event)

    def handleSwipe(self, end_pos):
        # Calculer la différence entre la position de départ et la position de fin
        delta_y = end_pos.y() - self.start_pos.y()

        # Seuil pour déterminer si le mouvement est un glissement
        swipe_threshold = 30

        if delta_y > swipe_threshold:
            # Glissement vers le bas - passer à l'élément suivant
            self.setCurrentIndex((self.currentIndex() + 1) % self.count())
        elif delta_y < -swipe_threshold:
            # Glissement vers le haut - passer à l'élément précédent
            self.setCurrentIndex((self.currentIndex() - 1) % self.count())

        # Réinitialiser la position de départ
        self.start_pos = None

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox avec navigation par glissement")

        # Layout principal
        layout = QVBoxLayout()

        # Créer une instance de SwipeComboBox
        combo_box = SwipeComboBox()
        combo_box.addItems(["Option 1", "Option 2", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 3", "Option 4", "Option 5"])

        # Ajouter le combo box au layout
        layout.addWidget(combo_box)

        # Configurer la fenêtre principale
        self.setLayout(layout)

# Application principale
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
