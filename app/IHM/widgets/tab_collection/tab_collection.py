from PyQt5.QtWidgets import QWidget

from app.IHM.widgets.tab_collection.ui_tab_collection import UiTabCollection
from app.lib.container import Container
from app.services.mangacollec import MangaCollec


class TabCollection(QWidget):
    def __init__(self, parent: QWidget):
        super(TabCollection, self).__init__(parent)

        self._container = Container()
        self.ui = UiTabCollection()
        self.ui.setup_ui(self)

        api: MangaCollec = self._container.get(MangaCollec)
        collection = api.get_v2_collection_by_username("shooterdev")
        self._container.set_parameter("possessions", collection)

        print("possessions", len(collection["possessions"]))
        print("reads", len(collection["reads"]))
        print("read_editions", len(collection["read_editions"]))
        print("volumes", len(collection["volumes"]))