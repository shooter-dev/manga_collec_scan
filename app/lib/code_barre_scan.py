from PyQt5.QtCore import QObject, pyqtSignal, QEvent, Qt
from PyQt5.QtGui import QKeyEvent


class CodeBarreScan(QObject):
    scan_completed = pyqtSignal(str)  # Signal pour indiquer qu'un scan est terminé

    def __init__(self):
        super().__init__()
        self._buffer = ""

    def eventFilter(self, obj, event):
        # Si l'événement est un keyPress (pression d'une touche)
        if event.type() == QEvent.KeyPress:
            key_event = event

            key = event.key()

            if key == Qt.Key_K:
                print("Escape key")

            print(event.text())
            # Si la touche pressée est un chiffre, on l'ajoute au _buffer
            if event.text().isdigit():
                self._buffer += event.text()
                # Garder uniquement les 13 derniers caractères
                self._buffer = self._buffer[-13:]
            # Si la touche Entrée est pressée (fin du scan)
            elif event.key() == Qt.Key_Return:
                self.process_scan()
                return True  # Empêche l'événement d'être traité par les autres widgets
        return super().eventFilter(obj, event)

    def process_scan(self):
        # Vérifier que le code est un EAN-13 (13 chiffres)
        if len(self._buffer) == 13 and self._buffer.isdigit() and self.is_valid_ean13(self._buffer):
            # Émettre un signal avec le code scanné
            self.scan_completed.emit(self._buffer)
        else:
            # Sinon, émettre un signal avec un message d'erreur
            self.scan_completed.emit("Erreur : Code EAN-13 invalide")
        # Réinitialiser le _buffer pour le prochain scan
        self._buffer = ""

    def is_valid_ean13(self, barcode):
        """Vérifie si le code-barres respecte la règle de contrôle EAN-13."""
        if len(barcode) != 13:
            return False
        total = sum(int(barcode[i]) * (3 if i % 2 else 1) for i in range(12))
        checksum = (10 - (total % 10)) % 10
        return checksum == int(barcode[-1])

