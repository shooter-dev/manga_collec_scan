from PyQt5.QtWidgets import QWidget, QHBoxLayout

from app.IHM.widgets.search_collection_header.ui_search_collection_header import UiSearchCollectionHeader


class SearchCollectionHeader(QWidget):
    def __init__(self, parent: QWidget):
        super(SearchCollectionHeader, self).__init__(parent)

        self.ui = UiSearchCollectionHeader()
        self.ui.setup_ui(self, QHBoxLayout)