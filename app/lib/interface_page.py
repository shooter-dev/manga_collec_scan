import importlib
from abc import ABC, abstractmethod, abstractproperty
from typing import Any, List

from PyQt5.QtWidgets import QWidget, QBoxLayout

from app.lib.container import Container
from app.lib.container_interface import ContainerInterface
from app.lib.router import Router


class InterfacePage(QWidget):
    _container: ContainerInterface
    router: Router = {}
    """
    Page interface de base pour toutes les pages
    """

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._container = Container()
        self.router = self._container.get(Router)
        # Importer dynamiquement la classe Ui associée à la page
        self.auto_instance_ui()

        self.ui = self.ui_class()  # Créer l'instance de la classe UI
        self.ui.setup_ui(window=self)  # Appliquer l'UI sur la page

    def auto_instance_ui(self):
        page_name = self.__class__.__name__  # Exemple : HomePage -> HomePage
        ui_class_name = f"Ui{self.__class__.__name__}"  # Exemple : HomePage -> UiHomePage
        module_name = f"app.IHM.pages.{page_name.lower().replace('page', '')}.{page_name.lower().replace('page', '')}_ui_page"  # Exemple : app.IHM.pages.home.home_ui_page
        self.ui_class = self.import_class(module_name, ui_class_name)

    @abstractmethod
    def page_update(self) -> Any:
        """Méthode à implémenter dans les pages spécifiques pour la mise à jour
        """
        pass

    @staticmethod
    def import_class(module_name: str, class_name: str):
        """Importer dynamiquement une classe en utilisant le nom du module et de la classe"""
        module = importlib.import_module(module_name)
        return getattr(module, class_name)
