from typing import Any

from PyQt5.QtWidgets import QHBoxLayout

from app.lib.interface_page import InterfacePage


class HomePage(InterfacePage):

    main_layout = QHBoxLayout

    def page_update(self) -> Any:
        print("Home Update Page")





