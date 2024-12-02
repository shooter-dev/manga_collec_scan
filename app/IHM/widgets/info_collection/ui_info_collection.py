from typing import Any

from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFormLayout

from app.const import FONT_42, FONT_26, FONT_16, FONT_12
from app.lib.interface_widget import InterfaceWidget


class UiInfoCollection(InterfaceWidget):
    def init(self, main_form: QWidget):
        main_form.setStyleSheet(u"""

                """)

    def create_widgets(self, main_form: QWidget) -> Any:
        self.value_tome = QLabel(main_form)
        self.value_tome.setObjectName(u"value_tome")

        self.tome_label = QLabel(main_form)
        self.tome_label.setObjectName(u"tome_label")

        self.value_edition = QLabel(main_form)
        self.value_edition.setObjectName(u"value_edition")

        self.edition_label = QLabel(main_form)
        self.edition_label.setObjectName(u"edition_label")

        self.stat_button = QPushButton(main_form)
        self.stat_button.setObjectName(u"stat_button")

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.value_tome.setFont(FONT_42)
        self.value_edition.setFont(FONT_26)
        self.value_edition.setFont(FONT_26)
        self.edition_label.setFont(FONT_16)

        self.stat_button.setFixedSize(QSize(57, 43))
        self.stat_button.setIcon(QIcon("app/assets/img/stat.png"))
        self.stat_button.setIconSize(QSize(14, 14))
        self.stat_button.setFont(FONT_12)

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(18, 20, 18, 15)
        self.label_layout = QFormLayout()
        self.label_layout.setObjectName(u"label_layout")
        self.label_layout.setLabelAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_layout.setFormAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_layout.setHorizontalSpacing(0)
        self.label_layout.setVerticalSpacing(0)

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.label_layout.setWidget(0, QFormLayout.LabelRole, self.value_tome)
        self.label_layout.setWidget(0, QFormLayout.FieldRole, self.tome_label)

        self.label_layout.setWidget(1, QFormLayout.LabelRole, self.value_edition)
        self.label_layout.setWidget(1, QFormLayout.FieldRole, self.edition_label)

        self.main_layout.addLayout(self.label_layout, Qt.AlignLeft | Qt.AlignVCenter)
        self.main_layout.addWidget(self.stat_button, 0, Qt.AlignRight | Qt.AlignTop)

    def setup_connections(self) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        main_form.setWindowTitle(QCoreApplication.translate("main_layout", u"Form", None))
        self.value_tome.setText(QCoreApplication.translate("main_layout", u"1384", None))
        self.value_edition.setText(QCoreApplication.translate("main_layout", u"352", None))
        self.tome_label.setText(QCoreApplication.translate("main_layout", u"TOMES", None))
        self.edition_label.setText(QCoreApplication.translate("main_layout", u"Editions", None))
        self.stat_button.setText(QCoreApplication.translate("main_layout", u"STAT", None))