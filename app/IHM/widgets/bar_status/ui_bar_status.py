import sys
from typing import Any

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QSpacerItem, QSizePolicy

from app.lib.interface_widget import InterfaceWidget


class UiBarStatus(InterfaceWidget):

    def init(self, main_form: QWidget):
        self.setMinimumHeight(24)
        self.setMaximumHeight(24)

    def create_widgets(self, main_form: QWidget) -> Any:
        self.title_app = QLabel(main_form)
        self.title_app.setObjectName("title_app")
        self.spacer = QSpacerItem(24,24,QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.button_close = QPushButton(self.title_app)

    def modify_widgets(self, main_form: QWidget) -> Any:
        size_btn = QSize(32, 32)
        self.button_close.setMinimumSize(size_btn)
        self.button_close.setMaximumSize(size_btn)
        self.button_close.setText("x")

        self.title_app.setText(main_form.parent().windowTitle().upper())

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(0, 0, 0, 0)

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.addWidget(self.title_app)
        self.main_layout.addSpacerItem(self.spacer)
        self.main_layout.addWidget(self.button_close)

    def setup_connections(self) -> Any:
        self.button_close.clicked.connect(self.on_action_exit_triggered)

    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass

    def on_action_exit_triggered(self):
        exit()