from typing import List, Dict, Tuple

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from app.IHM.widgets.news_header.ui_news_header import UiNewsHeader
from app.models.publisher import Publisher


class NewsHeader(QWidget):
    _publisher: List[Publisher] = []

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.ui = UiNewsHeader()
        self.ui.setup_ui(self,QHBoxLayout)

    def add_publisher_to_combo_box(self, publishers: List[Publisher]):
        self._publisher = publishers
        for publisher in self._publisher:
            self.ui.publisher_combo_box.addItem(publisher.title, publisher)




