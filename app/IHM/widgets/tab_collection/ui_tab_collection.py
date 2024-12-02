from typing import Any

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout

from app.IHM.widgets.info_collection.info_collection import InfoCollection
from app.const import STYLE_SCROLL_BAR
from app.lib.interface_widget import InterfaceWidget


class UiTabCollection(InterfaceWidget):
    def init(self, main_form: QWidget):
        pass

    def create_widgets(self, main_form: QWidget) -> Any:
        self.scroll_collection = QScrollArea(main_form)
        self.setObjectName("scroll_collection")

        self.scroll_collection_widget = QWidget(main_form)
        self.setObjectName("scroll_collection_widget")

        self.info_collection = InfoCollection(main_form)

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.info_collection.setFixedSize(QSize(656, 140))

        self.scroll_collection.setFixedSize(QSize(656, 386))
        self.scroll_collection.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_collection.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_collection.setWidgetResizable(True)
        self.scroll_collection.verticalScrollBar().setMinimumWidth(15)
        self.scroll_collection.verticalScrollBar().setMaximumWidth(15)
        self.scroll_collection.setStyleSheet(STYLE_SCROLL_BAR)

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_collection_layout = QVBoxLayout()

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.scroll_collection_widget.setLayout(self.scroll_collection_layout)
        self.scroll_collection.setWidget(self.scroll_collection_widget)

        #self.scroll_collection_layout.addWidget(self.info_collection)

    def setup_connections(self) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass