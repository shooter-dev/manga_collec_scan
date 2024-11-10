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

    def init_heure(self):
        self.timer_h = QTimer(self)
        self.timer_h.timeout.connect(self.update_time)
        self.timer_h.start(1000)  # Actualisation toutes les 1000 ms (1 seconde)

    def init_info(self):
        self.timer_info = QTimer(self)
        self.timer_info.timeout.connect(self.update_info)
        self.timer_info.start(10)  # Actualisation toutes les 1000 ms (1 seconde)

    def update_time(self):
        # Obtenir l'heure actuelle et l'afficher dans le label
        current_time = QTime.currentTime().toString('HH:mm:ss')
        self.ui.label_heure.setText(current_time)

    def update_info(self):
        #print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
        self.ui.label_cpu.setText(f" CPU: {psutil.cpu_percent(interval=1)}% ")
        virtual_memory = psutil.virtual_memory()
        #print(f"Total Memory: {virtual_memory.total / (1024 * 1024):.2f} MB")
        #print(f"Used Memory: {virtual_memory.used / (1024 * 1024):.2f} MB")
        self.ui.label_memory.setText(f" MEM: {virtual_memory.used / (1024 * 1024):.2f}/{virtual_memory.total / (1024 * 1024):.2f} MB ")
        net_io = psutil.net_io_counters()
        #print(f"Bytes Sent: {net_io.bytes_sent / (1024 * 1024):.2f} MB")
        self.ui.label_bytes_send.setText(f" S: {net_io.bytes_sent / (1024 * 1024):.2f} MB ")
        #print(f"Bytes Received: {net_io.bytes_recv / (1024 * 1024):.2f} MB")
        self.ui.label_bytes_rece.setText(f" R: {net_io.bytes_recv / (1024 * 1024):.2f} MB ")

