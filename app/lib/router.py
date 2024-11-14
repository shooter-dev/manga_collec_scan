from typing import Dict, Tuple, List

from PyQt5.QtWidgets import QWidget, QStackedWidget


class Router:

    __pages: Dict[str, Tuple[int, QWidget]] = {}
    __stacked: QStackedWidget = None

    def __init__(self, window: QWidget):
        self.window = window

    def add_stacked_widget(self, stacked: QStackedWidget):
        self.__stacked = stacked

    def add_page(self,name: str, page):
        window: "InterfacePage" = page(self.window)
        window.add_router(self)
        index = self.__stacked.addWidget(window)
        self.__pages[name] = (index, window)

    def call_page(self, name: str,param: List[object] = []):
        if name in self.__pages:
            index: int = 0
            page: "InterfacePage"

            index, page = self.__pages[name]
            self.__stacked.setCurrentIndex(index)
            page.page_update()

            print(f"call {name} | {page}")
        else:
            print(f"page {name} not found")