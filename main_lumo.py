import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, Q_ARG, pyqtSignal, QMetaObject
from pynput.keyboard import Key, Listener, KeyCode


class KeyMonitor(QtCore.QObject):
    keyPressed = pyqtSignal(KeyCode)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.listener = Listener(on_release=self.on_release)

    def on_release(self, key):
        # Émettre le signal dans le thread principal
        print(key)

    def emit_key(self, key):
        # Cette méthode émet le signal keyPressed
        self.keyPressed.emit(key)

    def stop_monitoring(self):
        self.listener.stop()

    def start_monitoring(self):
        self.listener.start()


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key Press Monitor")
        self.setGeometry(100, 100, 400, 300)

        self.label = QtWidgets.QLabel("Appuyez sur une touche...", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50, 100, 300, 50)

    def update_label(self, key):
        # Met à jour l'étiquette avec la touche pressée
        if isinstance(key, KeyCode):
            self.label.setText(f"Touche pressée : {key.char}")
        else:
            self.label.setText(f"Touche spéciale : {key}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Créer le widget principal et la fenêtre
    window = MainWindow()

    # Créer le moniteur de touches
    monitor = KeyMonitor()
    monitor.keyPressed.connect(window.update_label)
    monitor.start_monitoring()

    window.show()
    sys.exit(app.exec_())
