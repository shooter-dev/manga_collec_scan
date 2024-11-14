from typing import Any

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget

from app.const import RESOURCE_NEWS, RESOURCE_HOME, \
    RESOURCE_COLLECTION, RESOURCE_PLANNING, RESOURCE_SEARCH, RESOURCE_PANIER, RESOURCE_ACCOUNT, RESOURCE_ACCOUNT_HOVER, RESOURCE_PANIER_HOVER, RESOURCE_SEARCH_HOVER, RESOURCE_PLANNING_HOVER, \
    RESOURCE_COLLECTION_HOVER
from app.IHM.widgets.left_menu.ui_left_menu import Ui_LeftMenu
from app.lib.container import Container
from app.lib.container_interface import ContainerInterface
from app.lib.router import Router


class LeftMenu(QWidget):
    # router: Router = {}

    def __init__(self, parent: QWidget):

        super().__init__(parent)
        # self.c: ContainerInterface = Container()
        # self.router : Router = self.c.get(Router)
        # self.c.set("menu_lecture_item", self)

        self.ui = Ui_LeftMenu()
        self.ui.setup_ui(self, QHBoxLayout)

        self.setup_connections()


    def setup_connections(self) -> Any:
        self.ui.home_button.clicked.connect(self.on_button_home_clicked)
        self.ui.news_button.clicked.connect(self.on_button_news_clicked)
        self.ui.collection_button.clicked.connect(self.on_button_collection_clicked)
        self.ui.planning_button.clicked.connect(self.on_button_plannig_clicked)
        self.ui.search_button.clicked.connect(self.on_button_search_clicked)
        self.ui.panier_button.clicked.connect(self.on_button_panier_clicked)
        self.ui.account_button.clicked.connect(self.on_button_account_clicked)

    def add_router(self, router: Router):
        self.router = router

    def on_button_home_clicked(self):
        self.change_pages('home')

    def on_button_news_clicked(self):
        self.change_pages('news')

    def on_button_collection_clicked(self):
        self.change_pages('collection')

    def on_button_plannig_clicked(self):
        self.change_pages('planning')

    def on_button_search_clicked(self):
        self.change_pages('search')

    def on_button_panier_clicked(self):
        self.change_pages('panier')

    def on_button_account_clicked(self):
        self.change_pages('account')

    def change_pages(self, name):
        self.parent().parent().router.call_page(name)

    def change_icon_for_button(self, button: QPushButton, path_img: str):
        button.setIcon(QIcon(path_img))