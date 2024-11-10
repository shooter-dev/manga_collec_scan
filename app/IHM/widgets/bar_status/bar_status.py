import psutil
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from app.IHM.widgets.bar_status.ui_bar_status import UiBarStatus


class BarStatusWidget(QWidget):
    def __init__(self, parent: QWidget):
        super(BarStatusWidget, self).__init__(parent)

        self.ui = UiBarStatus()
        self.ui.setup_ui(self, QHBoxLayout)

        self.init_heure()
        self.init_info()

        net_io = psutil.net_io_counters()
        self.prev_bytes_sent = net_io.bytes_sent
        self.prev_bytes_recv = net_io.bytes_recv

    def init_heure(self):
        self.timer_h = QTimer(self)
        self.timer_h.timeout.connect(self.update_time)
        self.timer_h.start(1000)  # Actualisation toutes les 1000 ms (1 seconde)

    def init_info(self):
        self.timer_info = QTimer(self)
        self.timer_info.timeout.connect(self.update_info)
        self.timer_info.start(1000)  # Actualisation toutes les 1000 ms (1 seconde)

    def update_time(self):
        # Obtenir l'heure actuelle et l'afficher dans le label
        current_time = QTime.currentTime().toString('HH:mm:ss')
        self.ui.label_heure.setText(current_time)

    def update_info(self):
        self.ui.label_cpu.setText(f" CPU: {psutil.cpu_percent()}% ")

        virtual_memory = psutil.virtual_memory()
        self.ui.label_memory.setText(f" MEM: {virtual_memory.used / (1024 * 1024):.2f}/{virtual_memory.total / (1024 * 1024):.2f} MB ")

        self.update_debit()

    def update_debit(self):
        net_io = psutil.net_io_counters()
        bytes_sent_per_sec = (net_io.bytes_sent - self.prev_bytes_sent) / 1024  # en KB
        bytes_recv_per_sec = (net_io.bytes_recv - self.prev_bytes_recv) / 1024  # en KB
        self.prev_bytes_sent = net_io.bytes_sent
        self.prev_bytes_recv = net_io.bytes_recv
        self.ui.label_bytes_send.setText(f" S: {bytes_sent_per_sec:.2f} KB/s ")
        self.ui.label_bytes_rece.setText(f" R: {bytes_recv_per_sec:.2f} KB/s ")

