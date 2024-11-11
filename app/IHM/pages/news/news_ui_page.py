from typing import Any

from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtWidgets import QWidget, QLabel, QSpacerItem, QSizePolicy

from app.IHM.widgets.list_view_news.list_view_news import ListViewNews
from app.IHM.widgets.news_header.news_header import NewsHeader
from app.lib.interface_page import InterfacePage
from app.lib.interface_widget import InterfaceWidget


class UiNewsPage(InterfaceWidget):

    def init(self, main_form: QWidget):
        pass

    def create_widgets(self, main_form: QWidget) -> Any:
        self.header = NewsHeader(self)
        self.list_view_news = ListViewNews(self)

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.header.setFixedSize(QSize(720-88,51))
        self.list_view_news.resize(QSize(720-88, 1280-30-51))
        self.list_view_news.setAttribute(Qt.WA_AcceptTouchEvents, True)

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.addWidget(self.header, 0, Qt.AlignTop)
        self.main_layout.addWidget(self.list_view_news, 0, Qt.AlignBottom)

    def setup_connections(self) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass