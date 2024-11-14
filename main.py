import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication

from app.IHM.pages.window.main_windows import MainWindow
from app.lib.container import Container
from app.lib.container_interface import ContainerInterface


def main():

    app = QApplication(sys.argv)
    add_app_options(app)
    container: ContainerInterface = Container()

    size = recupere_dimension()
    window = MainWindow(size, container)
    window.show()
    sys.exit(app.exec_())


def add_app_options(app):
    app.setAttribute(Qt.AA_DisableHighDpiScaling, True)  # Désactiver la mise à l'échelle DPI
    app.setAttribute(Qt.AA_Use96Dpi, True)  # Forcer un DPI standard
    app.setDesktopFileName("MangaCollecScan")
    pass


def recupere_dimension() -> QSize:
    tab_dimention = sys.argv[1].split('x')
    win_width = int(tab_dimention[0])
    win_height = int(tab_dimention[1])
    return QSize(win_width, win_height)


if __name__ == '__main__':
    main()