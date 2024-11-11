from typing import Any

from PyQt5.QtCore import QSize, QCoreApplication, Qt
from PyQt5.QtGui import QPixmap, QFont, QPainter, QBrush, QColor
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy

from app.const import SIZE_IMAGE_NEWS_ITEM
from app.lib.interface_widget import InterfaceWidget


class ItemNewsUiWidget(InterfaceWidget):

    def create_widgets(self, main_form: QWidget) -> Any:
        self.image_volume_label = QLabel(main_form)
        self.image_volume_label.setObjectName(u"image_volume_label")

        self.name_serie_label = QLabel(main_form)
        self.name_serie_label.setObjectName(u"name_serie_label")

        self.font_8 = QFont()
        self.font_8.setPointSize(8)
        self.font_8.setFamily(U"Helvetica")

        self.font_14 = QFont()
        self.font_14.setPointSize(14)
        self.font_14.setFamily(U"Helvetica")

        self.vertical_spacer_2 = QSpacerItem(2, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vertical_spacer_4 = QSpacerItem(4, 4, QSizePolicy.Minimum, QSizePolicy.Fixed)



        self.name_tome_label = QLabel(main_form)
        self.name_tome_label.setObjectName(u"name_tome_label")

        self.sponso_label = QLabel(main_form)
        self.sponso_label.setObjectName(u"sponso_label")

    def modify_widgets(self, main_form: QWidget) -> Any:
        #style = f"QWidget {{ {PagesUtils.generer_background_color(0, 255) } }}"
        #main_form.setStyleSheet(style)
        self.__update_image_volume_label()

        self.__update_name_serie_label()

        self.__update_name_tome_label()

        self.__update_info_label()

    def __update_info_label(self):
        size = QSize(100, 17)
        self.sponso_label.setMinimumSize(size)
        self.sponso_label.setMaximumSize(size)
        self.sponso_label.setFont(self.font_8)
        self.sponso_label.setAlignment(Qt.AlignCenter)
        self.sponso_label.setStyleSheet(u"""
            border-color: rgb(28, 28, 30);
            border-style: solid;
            border-width: 1px;
            border-radius: 4px;
            padding-left: 4px;
            padding-right: 4px;
        """)

    def __update_name_tome_label(self):
        size = QSize(220, 17)
        self.name_tome_label.setMinimumSize(size)
        self.name_tome_label.setMaximumSize(size)
        self.name_tome_label.setFont(self.font_14)

    def __update_name_serie_label(self):
        size = QSize(220, 20)
        self.name_serie_label.setMinimumSize(size)
        self.name_serie_label.setMaximumSize(size)
        self.name_serie_label.setFont(self.font_14)

    def __update_image_volume_label(self):
        size = QSize(220, 330)
        self.image_volume_label.setMinimumSize(size)
        self.image_volume_label.setMaximumSize(size)

        pixmap = QPixmap(u"../../../assets/img/logo.png")

        # self.image_volume_label.setStyleSheet(u"""
        # #image_volume_label {
        #     border-style: inset;
        #     background-clip: border;
        #     border-width: 1px;
        #     border-radius: 9px; }
        # """)
        self.image_volume_label.setFixedSize(SIZE_IMAGE_NEWS_ITEM)
        self.image_volume_label.setAlignment(Qt.AlignCenter)
        self.image_volume_label.setPixmap(pixmap)
        self.image_volume_label.setScaledContents(True)

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(9, 9, 9, 9)

        self.info_horizontal_layout = QHBoxLayout()
        self.info_horizontal_layout.setObjectName(u"info_horizontal_layout")
        self.info_horizontal_layout.setSpacing(9)
        self.info_horizontal_layout.setContentsMargins(0, 0, 0, 0)

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.addWidget(self.image_volume_label, 0, Qt.AlignHCenter)

        self.main_layout.addItem(self.vertical_spacer_4)

        self.main_layout.addWidget(self.name_serie_label, 0, Qt.AlignLeft)

        self.main_layout.addItem(self.vertical_spacer_2)

        self.info_horizontal_layout.addWidget(self.name_tome_label, 0, Qt.AlignLeft)

        self.info_horizontal_layout.addWidget(self.sponso_label, 0, Qt.AlignLeft)

        self.main_layout.addLayout(self.info_horizontal_layout)

    def setup_connections(self, main_form: QWidget) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        main_form.setWindowTitle(QCoreApplication.translate("main_form", u"Form", None))
        self.image_volume_label.setText("")
        self.name_serie_label.setText(QCoreApplication.translate("main_form", u"My Love Story With Yamad...", None))
        self.name_tome_label.setText(QCoreApplication.translate("main_form", u"Tome 1", None))
        self.sponso_label.setText(QCoreApplication.translate("main_form", u"SPONSORIS\u00c9", None))
