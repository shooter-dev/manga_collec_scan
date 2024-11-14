from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget

from app.IHM.utils.image_download_thread import ImageDownloadThread


class ImageWidget(QLabel):
    pixmap: QPixmap
    pixmap_echec: QPixmap
    pixmap_chargement: QPixmap

    def __init__(self, parent: QWidget, loading_pix: QPixmap =None):
        super().__init__(parent)
        self.pixmap: QPixmap

        # Si une image de chargement est fournie, l'afficher par défaut
        if loading_pix is None:
            self.setText("Chargement... :)")  # Affiche un texte "chargement" si aucune image de chargement n'est fournie

        else:
            self.loading_pixmap = loading_pix
            self.setPixmap(self.loading_pixmap)  # Affiche l'image de chargement

    def load_url(self, url):
        """Télécharge et affiche l'image à partir de l'URL"""
        self.setText("Chargement...")  # Afficher un message pendant le téléchargement
        self.downloadThread = ImageDownloadThread(url)
        self.downloadThread.imageDownloaded.connect(self.updateImage)
        self.downloadThread.start()

    def set_pixmap_echec(self, pixmap: QPixmap):
        self.pixmap_echec = QPixmap(pixmap)


    def set_pixmap_chargement(self, pixmap: QPixmap):
        self.pixmap_chargement = QPixmap(pixmap)


    def updateImage(self, pixmap):
        if pixmap.isNull():
            if self.pixmap_echec.isNull():
                self.setText("Échec ... :(")
            else:
                self.setPixmap(self.pixmap_echec)
        else:
            self.setPixmap(pixmap)