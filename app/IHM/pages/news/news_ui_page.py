from typing import Any

from PyQt5.QtWidgets import QWidget, QLabel

from app.lib.interface_page import InterfacePage
from app.lib.interface_widget import InterfaceWidget


class UiNewsPage(InterfaceWidget):

    def init(self, main_form: QWidget):
        pass

    def create_widgets(self, main_form: QWidget) -> Any:
        self.label = QLabel(main_form)

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.label.setText("news ...")

    def create_layouts(self, main_form: QWidget) -> Any:
        pass

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.addWidget(self.label)

    def setup_connections(self) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass