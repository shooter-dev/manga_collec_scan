from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget

from app.IHM.utils.image_download_thread import ImageDownloadThread


class ImageWidget(QLabel):
    def __init__(self, parent: QWidget, loading_image_path=None):
        super().__init__(parent)
        self.pixmap = QPixmap()

        # Si une image de chargement est fournie, l'afficher par défaut
        if loading_image_path:
            self.loading_pixmap = QPixmap(loading_image_path)
            self.setPixmap(self.loading_pixmap)  # Affiche l'image de chargement
        else:
            self.setText("Chargement...")  # Affiche un texte "chargement" si aucune image de chargement n'est fournie

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