from typing import List

from PyQt5.QtWidgets import QStackedWidget

from app.lib.route import Route


class Router:
    __routes: List[Route] = []
    __stacked: QStackedWidget

    def __init__(self):
        pass

    def add_stacked_widget(self, stacked: QStackedWidget):
        self.__stacked = stacked

    def add_route(self, route: Route):
        window: "InterfacePage" = route.widget  # Prend la classe comme référence
        route.widget = window(self.__stacked.parent())  # Crée une instance de la classe
        route.index = self.__stacked.addWidget(route.widget)  # Ajoute l'instance au `QStackedWidget`
        self.__routes.append(route)

    def call_page(self, name: str):
        for route in self.__routes:
            if route.name == name:
                self.__stacked.setCurrentIndex(route.index)
                route.widget.page_update()
                return