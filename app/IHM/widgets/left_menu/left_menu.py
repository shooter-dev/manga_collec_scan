from typing import Any

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget

from app.const import RESOURCE_NEWS, RESOURCE_HOME, \
    RESOURCE_COLLECTION, RESOURCE_PLANNING, RESOURCE_SEARCH, RESOURCE_PANIER, RESOURCE_ACCOUNT, RESOURCE_ACCOUNT_HOVER, RESOURCE_PANIER_HOVER, RESOURCE_SEARCH_HOVER, RESOURCE_PLANNING_HOVER, \
    RESOURCE_COLLECTION_HOVER
from app.IHM.widgets.left_menu.ui_left_menu import Ui_LeftMenu


class LeftMenu(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.c: Container = Container()
        # self.r : Router = self.c.get(RouterInterface)
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

    def on_change_index(self, name: str):
        print("index", name)
        self.__clear_icon_button()

        if name == "news":
            print("Change News")
            self.ui.news_button.setIcon(QIcon(RESOURCE_HOME))
        elif name == "collection":
            print("Change Collection")
            self.ui.collection_button.setIcon(QIcon(RESOURCE_COLLECTION_HOVER))
        elif name == "planning":
            print("Change Planning")
            self.ui.planning_button.setIcon(QIcon(RESOURCE_PLANNING_HOVER))
        elif name == "search":
            print("Change Search")
            self.ui.search_button.setIcon(QIcon(RESOURCE_SEARCH_HOVER))
        elif name == "panier":
            print("Change Panier")
            self.ui.panier_button.setIcon(QIcon(RESOURCE_PANIER_HOVER))
        elif name == "account":
            print("Change Account")
            self.ui.account_button.setIcon(QIcon(RESOURCE_ACCOUNT_HOVER))

    def __clear_icon_button(self):
        self.ui.news_button.setIcon(QIcon(RESOURCE_NEWS))
        self.ui.collection_button.setIcon(QIcon(RESOURCE_COLLECTION))
        self.ui.planning_button.setIcon(QIcon(RESOURCE_PLANNING))
        self.ui.search_button.setIcon(QIcon(RESOURCE_SEARCH))
        self.ui.panier_button.setIcon(QIcon(RESOURCE_PANIER))
        self.ui.account_button.setIcon(QIcon(RESOURCE_ACCOUNT))

    def change_pages(self, name):
        # self.r.call(name)
        pass

    def change_icon_for_button(self, button: QPushButton, path_img: str):
        button.setIcon(QIcon(path_img))