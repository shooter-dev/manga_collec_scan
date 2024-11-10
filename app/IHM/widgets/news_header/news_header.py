from PyQt5.QtWidgets import QWidget, QHBoxLayout

from app.IHM.widgets.news_header.ui_news_header import UiNewsHeader


class NewsHeader(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.ui = UiNewsHeader()
        self.ui.setup_ui(self,QHBoxLayout)