import json
import sys

from PyQt5 import QtNetwork
from PyQt5.QtCore import QSize, Qt, QUrlQuery, QUrl, QByteArray, QObject, pyqtSignal
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtWidgets import QApplication

from app.IHM.pages.window.main_windows import MainWindow
from app.lib.container import Container
from app.lib.container_interface import ContainerInterface
from app.lib.router import Router
from app.services.mangacollec.mangacollec import MangaCollec

class PublisherLoader(QObject):
    # Signal pour envoyer les données chargées
    publishers_loaded = pyqtSignal(list)

    def __init__(self, api):
        super().__init__()
        self.api = api

    def load_publishers(self):
        """Fonction qui récupère les éditeurs et émet un signal quand c'est prêt."""
        publishers = self.api.get_publisher_all_v2().get('publishers', [])
        self.publishers_loaded.emit(publishers)  # Émet le signal avec les données récupérées


def main():

    app = QApplication(sys.argv)
    add_app_options(app)
    container: ContainerInterface = Container()
    size = recupere_dimension()


    router = Router()
    api_mangacollec = MangaCollec()

    container.set(Router,router)
    container.set(MangaCollec,api_mangacollec)

    container.set_parameter('publishers', api_mangacollec.get_publisher_all_v2()['publishers'])


    window = MainWindow(size, container, router)


    window.show()
    sys.exit(app.exec_())

def add_app_options(app):
    app.setAttribute(Qt.AA_DisableHighDpiScaling, True)  # Désactiver la mise à l'échelle DPI
    app.setAttribute(Qt.AA_Use96Dpi, True)  # Forcer un DPI standard
    app.setDesktopFileName("MangaCollecScan")
    pass


def recupere_dimension() -> QSize:
    tab_dimention = sys.argv[1].split('x')
    win_width = int(tab_dimention[0])
    win_height = int(tab_dimention[1])
    return QSize(win_width, win_height)


if __name__ == '__main__':
    main()