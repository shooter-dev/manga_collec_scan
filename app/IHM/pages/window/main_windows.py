from typing import Dict, Tuple

from PyQt5.QtCore import QSize, QEvent
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QApplication, QWidget

from app.IHM.pages.home.home_page import HomePage
from app.IHM.pages.news.news_page import NewsPage
from app.lib.code_barre_scan import CodeBarreScan
from app.lib.container import Container
from app.lib.container_interface import ContainerInterface
from app.lib.interface_page import InterfacePage
from app.IHM.pages.window.ui_main_window import UiMainWindow
from app.lib.router import Router


class MainWindow(QMainWindow):
    dim: QSize
    router: Router = {}

    def __init__(self, size: QSize, container: ContainerInterface):
        super().__init__()
        print(f"Main: {self}")
        self.dim = size
        container.set(Router, Router(self))
        self.router = container.get(Router)

        self.ui = UiMainWindow()
        self.ui.setup_ui(window=self,layout=QVBoxLayout)
        self.router.add_stacked_widget(self.ui.pages_stack)
        #self.ui.menu.add_router(self.__router)

        self.add_pages()

        self.router.call_page('news')

        # self.code_barre_scan = CodeBarreScan()

        # # Connecter le signal scan_completed à une méthode pour afficher le résultat
        # self.code_barre_scan.scan_completed.connect(self.on_scan_completed)
        #
        # # Installer le filtre d'événements sur la fenêtre principale pour capter les événements clavier
        # self.installEventFilter(self.code_barre_scan)


    def add_pages(self):
        self.router.add_page("home", HomePage)
        self.router.add_page("news", NewsPage)

    def on_scan_completed(self, message):
        """Affiche le message du scan (code ou erreur)"""
        print(message)

    def exit_app(self):
        print("Nettoyage avant de quitter...")
        self.deleteLater()  # Planifie la suppression de l'objet
        QApplication.quit()

