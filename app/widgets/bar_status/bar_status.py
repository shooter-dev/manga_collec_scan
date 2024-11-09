from PyQt5.QtWidgets import QWidget, QHBoxLayout

from app.widgets.bar_status.ui_bar_status import UiBarStatus


class BarStatusWidget(QWidget):
    def __init__(self, parent: QWidget):
        super(BarStatusWidget, self).__init__(parent)
        self.ui = UiBarStatus()
        self.ui.setup_ui(self, QHBoxLayout)



