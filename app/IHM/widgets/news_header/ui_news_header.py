from typing import Any

from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox

from app.const import FONT_18, FONT_16
from app.lib.interface_widget import InterfaceWidget


class UiNewsHeader(InterfaceWidget):
    def init(self, main_form: QWidget):
        pass

    def create_widgets(self, main_form: QWidget) -> Any:
        self.name_page_label = QLabel(main_form)
        self.name_page_label.setObjectName(u"name_page_label")

        self.publisher_combo_box = QComboBox(main_form)
        self.publisher_combo_box.setObjectName(u"publisher_combo_box")

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.__update_name_page_label()

        self.__update_publisher_combo_box()

    def __update_publisher_combo_box(self):
        self.publisher_combo_box.setFixedSize(QSize(200, 28))
        self.publisher_combo_box.setFont(FONT_16)
        self.publisher_combo_box.font().bold()
        #delegate = SizeDelegateComboBoxPublisher(self.publisher_combo_box)
        self.publisher_combo_box.setMaxVisibleItems(5)

        #self.publisher_combo_box.setItemDelegate(delegate)
        self.publisher_combo_box.setEditable(True)
        self.publisher_combo_box.setStyleSheet(u"""
            #publisher_combo_box {
                font-size: 17px;               /* Taille de la police */
                background-color: #FFF;   /* Couleur de fond */
                color: darkblue;               /* Couleur du texte */
                border: none;
                text-align: right;
                /* border: 1px solid blue;        Bordure du ComboBox */
            }
            #publisher_combo_box::drop-down {
                border: none;                   /* Largeur de la flèche */
            }
            #publisher_combo_box::down-arrow {
                image: url(:/icons/icons/red/arrow-combo-box.svg);    /* Remplacez par le chemin de votre image de flèche */
                width: 28px;
                height: 28px;
                margin-right: 28px;
            }
        """)
        line_edit = self.publisher_combo_box.lineEdit()
        line_edit.setAlignment(Qt.AlignRight)
        line_edit.setReadOnly(True)

        self.publisher_combo_box.addItem("")

    def __add_item_publisher_combo_box(self):
        icon = QIcon()
        icon.addFile(u":/img/img/logo.png", QSize(), QIcon.Disabled, QIcon.Off)

    def __update_name_page_label(self):
        self.name_page_label.setFixedSize(QSize(300, 21))
        self.name_page_label.setFont(FONT_18)

    def create_layouts(self, main_form: QWidget) -> Any:
        pass

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.addWidget(self.name_page_label, 0, Qt.AlignLeft | Qt.AlignVCenter)

        self.main_layout.addWidget(self.publisher_combo_box, 0, Qt.AlignRight | Qt.AlignVCenter)

    def setup_connections(self) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        self.name_page_label.setText(QCoreApplication.translate("HeaderNews", u"Nouveaut\u00e9s", None))
        self.publisher_combo_box.setItemText(0, QCoreApplication.translate("HeaderNews", u"Editeurs", None))

        self.publisher_combo_box.setCurrentText(QCoreApplication.translate("HeaderNews", u"Editeurs", None))