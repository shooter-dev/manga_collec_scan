from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout

from app.IHM.pages.home.home_page import HomePage
from app.IHM.pages.news.news_page import NewsPage
from app.lib.window.ui_main_window import UiMainWindow


class MainWindow(QMainWindow):
    dim: QSize

    def __init__(self, size: QSize):
        super().__init__()
        self.dim = size

        self.ui = UiMainWindow()
        self.ui.setup_ui(self,QVBoxLayout)

        self.page_home = HomePage(self)
        self.page_news = NewsPage(self)

        self.ui.pages_stack.addWidget(self.page_home)
        self.ui.pages_stack.addWidget(self.page_news)

        self.ui.pages_stack.setCurrentIndex(1)

    # def applicationSupportsSecureRestorableState(self) -> bool:
    #     return True