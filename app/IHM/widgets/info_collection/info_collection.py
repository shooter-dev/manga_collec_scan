from PyQt5.QtWidgets import QWidget

from app.IHM.widgets.info_collection.ui_info_collection import UiInfoCollection


class InfoCollection(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.ui = UiInfoCollection()
        self.ui.setup_ui(self)