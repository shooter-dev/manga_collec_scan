from abc import abstractmethod
from typing import Any

from PyQt5.QtCore import QMetaObject
from PyQt5.QtWidgets import QWidget, QBoxLayout


class InterfaceWidget(QWidget):
    """
    Page interface
    """
    def setup_ui(self, window: QWidget, layout) -> Any:

        self.main_layout: QBoxLayout = layout(window)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.init(window)
        self.create_widgets(window)
        self.modify_widgets(window)
        self.create_layouts(window)
        self.widgets_to_layouts(window)
        self.setup_connections()

        if not window.objectName():
            window.setObjectName(u"main_form")
        self.retranslate_ui(window)
        QMetaObject.connectSlotsByName(window)

    @abstractmethod
    def init(self, main_form: QWidget):
        pass

    @abstractmethod
    def create_widgets(self, main_form: QWidget) -> Any:
        pass

    @abstractmethod
    def modify_widgets(self, main_form: QWidget) -> Any:
        pass

    @abstractmethod
    def create_layouts(self, main_form: QWidget) -> Any:
        pass

    @abstractmethod
    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        pass

    @abstractmethod
    def setup_connections(self) -> Any:
        pass

    @abstractmethod
    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass