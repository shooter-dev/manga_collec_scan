import sys
from typing import Any

from PyQt5.QtCore import QSize, QCoreApplication, Qt, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QSpacerItem, QSizePolicy, QApplication, QMainWindow

from app.const import FONT_18, FONT_16, RESOURCE_CPU, RESOURCE_HOME, RESOURCE_PLANNING, RESOURCE_BYTES_SEND, \
    RESOURCE_BYTES_RECE, FONT_12
from app.lib.interface_widget import InterfaceWidget


class UiBarStatus(InterfaceWidget):

    def init(self, main_form: QWidget):
        self.parent = main_form

    def create_widgets(self, main_form: QWidget) -> Any:
        self.label_heure = QLabel(main_form)
        self.label_cpu = QLabel(main_form)
        self.image_cpu = QLabel(main_form)
        self.label_memory = QLabel(main_form)
        self.label_bytes_send = QLabel(main_form)
        self.image_bytes_send = QLabel(main_form)
        self.label_bytes_rece = QLabel(main_form)
        self.image_bytes_rece = QLabel(main_form)
        self.title_app = QLabel(main_form)
        self.title_app.setObjectName("title_app")
        self.spacer = QSpacerItem(24,24,QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.button_close = QPushButton(self.title_app)

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.label_heure.setFont(FONT_16)
        self.label_heure.setText(" 00:00 ")

        self.label_cpu.setFont(FONT_16)
        self.label_cpu.setText("CPU --- % ")
        self.image_cpu.setPixmap(QPixmap(RESOURCE_CPU))
        self.image_cpu.setScaledContents(True)
        self.image_cpu.setFixedSize(QSize(24,24))

        self.label_memory.setFont(FONT_16)
        self.label_memory.setText("MEM -- MB ")

        self.label_bytes_send.setFont(FONT_12)
        self.label_bytes_send.setText("Send -- MB ")
        self.image_bytes_send.setPixmap(QPixmap(RESOURCE_BYTES_SEND))
        self.image_bytes_send.setScaledContents(True)
        self.image_bytes_send.setFixedSize(QSize(24,24))

        self.label_bytes_rece.setFont(FONT_12)
        self.label_bytes_rece.setText("Rece -- MB ")
        self.image_bytes_rece.setPixmap(QPixmap(RESOURCE_BYTES_RECE))
        self.image_bytes_rece.setScaledContents(True)
        self.image_bytes_rece.setFixedSize(QSize(24,24))

        size_btn = QSize(30, 30)
        self.button_close.setMinimumSize(size_btn)
        self.button_close.setMaximumSize(size_btn)
        #self.button_close.setText("x")

        #self.title_app.setText(main_form.parent().windowTitle().upper())

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(2)

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.addWidget(self.label_heure, 0, Qt.AlignLeft|Qt.AlignVCenter)
        self.main_layout.addWidget(self.title_app, 0, Qt.AlignHCenter|Qt.AlignVCenter)
        self.main_layout.addSpacerItem(self.spacer)
        self.main_layout.addWidget(self.image_cpu, 0, Qt.AlignRight|Qt.AlignVCenter)
        self.main_layout.addWidget(self.label_cpu, 0, Qt.AlignRight|Qt.AlignVCenter)
        self.main_layout.addWidget(self.label_memory, 0, Qt.AlignRight|Qt.AlignVCenter)
        self.main_layout.addWidget(self.image_bytes_rece, 0, Qt.AlignRight|Qt.AlignVCenter)
        self.main_layout.addWidget(self.label_bytes_rece, 0, Qt.AlignRight|Qt.AlignVCenter)
        self.main_layout.addWidget(self.image_bytes_send, 0, Qt.AlignRight|Qt.AlignVCenter)
        self.main_layout.addWidget(self.label_bytes_send, 0, Qt.AlignRight|Qt.AlignVCenter)
        self.main_layout.addWidget(self.button_close, 0, Qt.AlignRight|Qt.AlignVCenter)

    def setup_connections(self) -> Any:
        self.button_close.clicked.connect(self.on_action_exit_triggered)

    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass

    def on_action_exit_triggered(self):
        p = self.parent.parent()
        print(self.parent.parent())

        if isinstance(p, QMainWindow):  # Vérifie que le parent est un QWidget
            p.close()
        else:
            QCoreApplication.instance().quit()  # Quitter l'application si aucun parent valide n'est trouvé