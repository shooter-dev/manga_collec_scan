from typing import Any

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

from app.IHM.pages.collection.collection_ui_page import UiCollectionPage
from app.lib.controller import Controller


class CollectionPage(Controller):
    ui: UiCollectionPage
    main_layout = QVBoxLayout

    def page_update(self) -> Any:
        print("Collection Update Page")





