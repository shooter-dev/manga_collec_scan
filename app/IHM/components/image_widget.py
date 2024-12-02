from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget

from app.IHM.utils.image_download_thread import ImageDownloadThread


class ImageWidget(QLabel):

    _cache = {}
    pixmap: QPixmap
    pixmap_echec: QPixmap = None
    pixmap_chargement: QPixmap = None

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

        # Vérifier si l'image est dans le cache
        if url in self._cache:
            #print(f"Image chargée depuis le cache pour l'URL : {url}")
            self.setPixmap(self._cache[url])
            return

            # Afficher l'image de chargement si définie
        if self.pixmap_chargement:
            self.setPixmap(self.pixmap_chargement)
        else:
            self.setText("Chargement...")

        self.downloadThread = ImageDownloadThread(url)
        self.downloadThread.imageDownloaded.connect(lambda pixmap: self.updateImage(url, pixmap))
        self.downloadThread.start()

    def set_pixmap_echec(self, pixmap: QPixmap):
        self.pixmap_echec = QPixmap(pixmap)


    def set_pixmap_chargement(self, pixmap: QPixmap):
        self.pixmap_chargement = QPixmap(pixmap)


    def updateImage(self, url, pixmap):
        if pixmap.isNull():
            # Afficher l'image d'échec ou un texte par défaut
            if self.pixmap_echec:
                self.setPixmap(self.pixmap_echec)
            else:
                self.setText("Échec ... :(")
        else:
            # Ajouter l'image au cache
            self._cache[url] = pixmap
            #print(f"Image mise en cache pour l'URL : {url}")
            # Afficher l'image téléchargée
            self.setPixmap(pixmap)