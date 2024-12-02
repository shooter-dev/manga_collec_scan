import importlib
from abc import abstractmethod

from PyQt5.QtWidgets import QWidget, QBoxLayout

from app.IHM.utils.controler_util import auto_instance_ui
from app.lib.container import Container
from app.lib.container_interface import ContainerInterface
from app.lib.interface_widget import InterfaceWidget
from app.lib.router import Router


class Controller(QWidget):
    container: ContainerInterface
    router: Router
    ui: InterfaceWidget

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.container = Container()
        self.router = self.container.get(Router)

        #Importer dynamiquement la vue au controller
        self.ui = auto_instance_ui(self)
        self.ui.setup_ui(window=self)  # Appliquer l'UI sur la page

    @abstractmethod
    def page_update(self) -> None: ...

