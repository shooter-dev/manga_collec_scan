from PyQt5.QtCore import QObject, pyqtSignal, QEvent, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel


class CodeBarreScan(QObject):
    scan_completed = pyqtSignal(str)  # Signal pour indiquer qu'un scan est terminé

    def __init__(self):
        super().__init__()
        self._buffer = ""

    def eventFilter(self, obj, event):
        """Filtre les événements clavier pour gérer la saisie du code-barres"""
        if event.type() == QEvent.KeyPress:
            key = event.text()

            # Si la touche pressée est un chiffre, on l'ajoute au _buffer
            if key.isdigit():
                self._buffer += key
                # Garder uniquement les 13 derniers caractères
                self._buffer = self._buffer[-13:]
            # Si la touche Entrée est pressée, on termine le scan
            elif event.key() == Qt.Key_Return:
                self.process_scan()
                return True  # Empêche l'événement d'être traité par les autres widgets

            # Si la touche Escape est pressée, réinitialiser le buffer
            elif event.key() == Qt.Key_Escape:
                self._buffer = ""  # Réinitialise le buffer en cas d'annulation
                return True

        return super().eventFilter(obj, event)

    def process_scan(self):
        """Traite le scan et valide le code-barres"""
        if len(self._buffer) == 13 and self._buffer.isdigit() and self.is_valid_ean13(self._buffer):
            self.scan_completed.emit(self._buffer)  # Code-barres valide
        else:
            self.scan_completed.emit("Erreur : Code EAN-13 invalide")  # Code-barres invalide
        # Réinitialiser le buffer pour le prochain scan
        self._buffer = ""

    def is_valid_ean13(self, barcode):
        """Vérifie si le code-barres respecte la règle de contrôle EAN-13."""
        if len(barcode) != 13:
            return False
        total = sum(int(barcode[i]) * (3 if i % 2 else 1) for i in range(12))
        checksum = (10 - (total % 10)) % 10
        return checksum == int(barcode[-1])


# Exemple d'utilisation avec un widget (par exemple un QMainWindow)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialiser le scanner de code-barres
        self.code_barre_scan = CodeBarreScan()

        # Connecter le signal scan_completed à une méthode pour afficher le résultat
        self.code_barre_scan.scan_completed.connect(self.on_scan_completed)

        # Installer le filtre d'événements sur l'application entière pour capter les événements clavier
        QApplication.instance().installEventFilter(self.code_barre_scan)

        # Exemple d'ajout de widgets dans la fenêtre principale
        self.setWindowTitle("Scanner de code-barres")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.label = QLabel("Scannez un code-barres...")
        self.input = QLineEdit()
        self.button = QPushButton("Valider")

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_scan_completed(self, message):
        """Affiche le message du scan (code ou erreur)"""
        self.label.setText(f"Scan terminé : {message}")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
