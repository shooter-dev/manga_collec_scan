from typing import Any

from PyQt5.QtCore import QObject, Qt, QRect
from PyQt5.QtWidgets import QStackedWidget, QVBoxLayout, QWidget, QBoxLayout, QHBoxLayout

from app.widgets.bar_status.bar_status import BarStatusWidget
from app.widgets.left_menu.left_menu import LeftMenu
from main_test import MainWindow


class UiMainWindow(QObject):

    def setup_ui(self, window: MainWindow, layout: QBoxLayout) -> Any:
        self.init_page(window)
        self.create_widgets(window)
        self.modify_widgets(window)
        self.create_layouts(layout)
        self.widgets_to_layouts(window)

    def init_page(self, win: MainWindow):
        win.setWindowFlag(Qt.FramelessWindowHint)
        win.setGeometry(QRect(60, 0, 800, 480))
        #win.showFullScreen()
        win.resize(win.dim)
        win.setMinimumSize(win.dim)
        win.setMaximumSize(win.dim)
        win.setWindowTitle('PyQt5 GUI MangaCollecScan')

    def create_widgets(self, win):
        self.widget = QWidget(win)
        self.widget.setObjectName(u"centralWidget")
        win.setCentralWidget(self.widget)

        self.bar = BarStatusWidget(win)  # Barre de statut en haut
        self.menu = LeftMenu(win)  # Menu latéral
        self.pages_stack = QStackedWidget(win)  # Zone pour le contenu principal

    def modify_widgets(self, win):
        pass

    def create_layouts(self, layout):
        self.main_layout: QBoxLayout = layout(self.widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.body_layout = QHBoxLayout()  # Pas besoin de l'attacher à `self.widget`
        self.body_layout.setSpacing(0)
        self.body_layout.setContentsMargins(0, 0, 0, 0)

    def widgets_to_layouts(self, win):
        self.main_layout.addWidget(self.bar)  # Ajoute la barre de statut au layout principal
        self.main_layout.addLayout(self.body_layout)  # Ajoute le layout secondaire au layout principal

        self.body_layout.addWidget(self.menu)
        self.body_layout.addWidget(self.pages_stack)  # Ajout unique de pages_stack au layout secondaire