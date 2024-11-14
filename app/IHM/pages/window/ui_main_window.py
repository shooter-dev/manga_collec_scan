from typing import Any

from PyQt5.QtCore import QObject, Qt, QRect, QSize
from PyQt5.QtWidgets import QStackedWidget, QWidget, QBoxLayout, QHBoxLayout

from app.IHM.widgets.bar_status.bar_status import BarStatusWidget
from app.IHM.widgets.left_menu.left_menu import LeftMenu


class UiMainWindow(QObject):

    def setup_ui(self, window, layout: type(QBoxLayout)) -> Any:
        self.init_page(window)
        self.create_widgets(window)
        self.modify_widgets(window)
        self.create_layouts(layout)
        self.widgets_to_layouts(window)

    def init_page(self, win: "MainWindow"):
        win.setWindowFlag(Qt.FramelessWindowHint)
        win.setWindowTitle('PyQt5 GUI MangaCollecScan')
        win.setGeometry(QRect(60, 0, 800, 480))
        #win.showFullScreen()
        win.resize(win.dim)
        win.setMinimumSize(win.dim)
        win.setMaximumSize(win.dim)
        win.setStyleSheet(U""" background-color: #FFF;   /* Couleur de fond */""")

    def create_widgets(self, win):
        self.widget = QWidget(win)
        self.widget.setObjectName(u"centralWidget")
        win.setCentralWidget(self.widget)

        self.bar = BarStatusWidget(win)  # Barre de statut en haut
        self.menu = LeftMenu(win)  # Menu latéral
        self.pages_stack = QStackedWidget(win)  # Zone pour le contenu principal

    def modify_widgets(self, win):
        size_bar = QSize(720, 30)
        size_menu = QSize(84, 1280 - size_bar.height())
        size_pages = QSize(720 - size_menu.width(), 1280 - size_bar.height())

        self.bar.setFixedSize(size_bar)
        self.menu.setFixedSize(size_menu)
        self.pages_stack.setFixedSize(size_pages)

    def create_layouts(self, layout):
        self.main_layout: QBoxLayout = layout(self.widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.body_layout = QHBoxLayout()  # Pas besoin de l'attacher à `self.widget`
        self.body_layout.setSpacing(0)
        self.body_layout.setContentsMargins(0, 0, 0, 0)

    def widgets_to_layouts(self, win):
        self.main_layout.addWidget(self.bar, 0, Qt.AlignTop)  # Ajoute la barre de statut au layout principal
        self.main_layout.addLayout(self.body_layout)  # Ajoute le layout secondaire au layout principal

        self.body_layout.addWidget(self.menu, 0, Qt.AlignLeft)
        self.body_layout.addWidget(self.pages_stack, 0, Qt.AlignRight)  # Ajout unique de pages_stack au layout secondaire
