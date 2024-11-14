import requests
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtGui import QPixmap


class ImageDownloadThread(QThread):
    # Signal émis lorsque l'image est téléchargée
    imageDownloaded = pyqtSignal(QPixmap)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            # Télécharger l'image à partir de l'URL
            response = requests.get(self.url)
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.imageDownloaded.emit(pixmap)  # Émettre le signal une fois l'image téléchargée

        except Exception as e:
            print(f"Erreur lors du téléchargement de l'image: {e}")
            self.imageDownloaded.emit(QPixmap())  # Émettre une image vide en cas d'erreur