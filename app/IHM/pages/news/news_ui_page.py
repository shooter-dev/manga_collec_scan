from typing import Any

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QSpacerItem, QSizePolicy

from app.IHM.widgets.news_header.news_header import NewsHeader
from app.lib.interface_page import InterfacePage
from app.lib.interface_widget import InterfaceWidget


class UiNewsPage(InterfaceWidget):

    def init(self, main_form: QWidget):
        pass

    def create_widgets(self, main_form: QWidget) -> Any:
        self.header: NewsHeader = NewsHeader(self)
        #self.item_news = ViewListItemNewsWidget(self)
        self.item_news = QWidget(self)

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.header.setFixedSize(QSize(720-88,51))
        self.item_news.setFixedSize(QSize(720-78,1000))

    def create_layouts(self, main_form: QWidget) -> Any:
        pass

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.addWidget(self.header,0 , Qt.AlignTop)
        self.main_layout.addWidget(self.item_news)

    def setup_connections(self) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass