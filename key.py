from PyQt5.QtCore import Qt


class KeyPressHandler:
    def __init__(self, window):
        self.window = window

    def keyPressEvent(self, event):
        """Gérer les événements clavier"""
        if event.key() == Qt.Key_A:
            self.window.show_popup("Vous avez appuyé sur 'A'!")
            self.window.current_page = 1  # Passer à la page 2
            self.window.stacked_widget.setCurrentIndex(self.window.current_page)

        elif event.key() == Qt.Key_B:
            self.window.show_popup("Vous avez appuyé sur 'B'!")
            self.window.current_page = 0  # Passer à la page 1
            self.window.stacked_widget.setCurrentIndex(self.window.current_page)

        else:
            # Permet de gérer d'autres touches ou de déléguer à la méthode par défaut
            event.ignore()