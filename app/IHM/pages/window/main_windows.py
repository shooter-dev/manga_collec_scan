from typing import Dict, Tuple

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QApplication, QWidget

from app.IHM.pages.home.home_page import HomePage
from app.IHM.pages.news.news_page import NewsPage
from app.lib.code_barre_scan import CodeBarreScan
from app.lib.interface_page import InterfacePage
from app.IHM.pages.window.ui_main_window import UiMainWindow


class MainWindow(QMainWindow):
    dim: QSize
    __pages: Dict[str, Tuple[int, QWidget]] = {}

    def __init__(self, size: QSize):
        super().__init__()
        self.dim = size

        self.ui = UiMainWindow()
        self.ui.setup_ui(self,QVBoxLayout)

        self.add_pages()

        self.call_page('news')

        self.scanner = CodeBarreScan()
        self.installEventFilter(self.scanner)

        self.scanner.scan_completed.connect(self.display_result)


    def add_pages(self):
        self.add_page("home", HomePage)
        self.add_page("news", NewsPage)

    def add_page(self,name: str, page):
        window = page(self)
        index = self.ui.pages_stack.addWidget(window)
        self.__pages[name] = (index, window)


    def call_page(self, name: str):
        if name in self.__pages:
            index: int = 0
            page: InterfacePage

            index, page = self.__pages[name]
            self.ui.pages_stack.setCurrentIndex(index)
            page.page_update()

            print(f"call {name} | {page}")

    def display_result(self, result):
        # Afficher le résultat du scan
        #self.result_label.setText(result)
        print(result)

    def exit_app(self):
        print("Nettoyage avant de quitter...")
        self.deleteLater()  # Planifie la suppression de l'objet
        QApplication.quit()
