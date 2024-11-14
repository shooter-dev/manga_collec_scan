from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget

from app.IHM.utils.image_download_thread import ImageDownloadThread


class ImageWidget(QLabel):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.pixmap = QPixmap()

    def load_url(self, url):
        """Télécharge et affiche l'image à partir de l'URL"""
        self.setText("Chargement...")  # Afficher un message pendant le téléchargement
        self.downloadThread = ImageDownloadThread(url)
        self.downloadThread.imageDownloaded.connect(self.updateImage)
        self.downloadThread.start()

    def updateImage(self, pixmap):
        if pixmap.isNull():
            self.setText("Échec du téléchargement")
        else:
            self.setPixmap(pixmap)