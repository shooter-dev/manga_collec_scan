from typing import Any

from PyQt5.QtWidgets import QHBoxLayout

from app.IHM.pages.home.home_ui_page import UiHomePage
from app.lib.controller import Controller


class HomePage(Controller):
    main_layout = QHBoxLayout
    ui: UiHomePage

    def page_update(self) -> Any:
        print("Home Update Page")





