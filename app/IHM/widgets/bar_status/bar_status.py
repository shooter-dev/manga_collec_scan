from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from app.IHM.widgets.bar_status.ui_bar_status import UiBarStatus


class BarStatusWidget(QWidget):
    def __init__(self, parent: QWidget):
        super(BarStatusWidget, self).__init__(parent)

        self.ui = UiBarStatus()
        self.ui.setup_ui(self, QHBoxLayout)

        self.init_heure()

    def init_heure(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Actualisation toutes les 1000 ms (1 seconde)

    def update_time(self):
        # Obtenir l'heure actuelle et l'afficher dans le label
        current_time = QTime.currentTime().toString('HH:mm:ss')
        self.ui.label_heure.setText(current_time)
