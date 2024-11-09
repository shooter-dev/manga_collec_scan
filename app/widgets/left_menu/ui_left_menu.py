from typing import Any

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QFrame

from app.const import STYLE_COLOR_PRIMARY, STYLE_COLOR_STATE_HOVER, STYLE_COLOR_BORDER, SIZE_BUTTON_MENU, \
    SIZE_ICON_BUTTON_MENU, ICON_HOME, ICON_NEWS, ICON_COLLECTION, ICON_PLANNING, ICON_SEARCH, ICON_PANIER, ICON_ACCOUNT, \
    RESOURCE_HOME

from app.lib.interface_widget import InterfaceWidget

#import app.assets.resources



class Ui_LeftMenu(InterfaceWidget):

    def init(self, main_form: QWidget):
        size = QSize(67, 480)
        main_form.setMinimumSize(size)
        main_form.setMaximumSize(size)
        main_form.setStyleSheet(f"""
            QWidget {{
                border-right-color: {STYLE_COLOR_BORDER};
                border-right-style :solid;
                border-right-width: 3px;
            }}
            
            QPushButton {{
                border: 0px solid {STYLE_COLOR_BORDER};
                border-radius: 23px;
                padding-left: 9px;
                padding-right: 9px;
            }}
            
            QPushButton:hover {{
                border: 1px solid {STYLE_COLOR_BORDER};
                background: {STYLE_COLOR_STATE_HOVER};
                border-radius: 23px;
            }}
            
            #home_button {{
            
                border: 1px solid {STYLE_COLOR_PRIMARY};
                border-image: url('{RESOURCE_HOME}') 0 0 0 0 stretch stretch;
            }}
            Line {{
	            background-color: #000;
            }}
        """)

    def create_widgets(self, main_form: QWidget) -> Any:
        self.spacer_10_v = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.spacer_8_v = QSpacerItem(10, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.spacer_buttom = QSpacerItem(10, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.home_button = QPushButton(main_form)
        self.home_button.setObjectName(u"home_button")

        self.news_button = QPushButton(main_form)
        self.news_button.setObjectName(u"news_button")
        
        self.collection_button = QPushButton(main_form)
        self.collection_button.setObjectName(u"collection_button")

        self.planning_button = QPushButton(main_form)
        self.planning_button.setObjectName(u"planning_button")
        
        self.search_button = QPushButton(main_form)
        self.search_button.setObjectName(u"search_button")
        
        self.panier_button = QPushButton(main_form)
        self.panier_button.setObjectName(u"panier_button")

        self.account_button = QPushButton(main_form)
        self.account_button.setObjectName(u"account_button")

        self.line = QFrame(main_form)
        self.line.setObjectName(u"line")

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.__update_init_home_button()
        self.__update_init_news_button()
        self.__update_collection_button()
        self.__update_planning_button()
        self.__update_search_button()
        self.__update_panier_button()
        self.__update_account_button()

        self.line.setMinimumSize(QSize(1, 480))
        self.line.setMaximumSize(QSize(1, 480))
        self.line.setFrameShape(QFrame.NoFrame)
        self.line.setFrameShadow(QFrame.Plain)

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(0, 8, 0, 10)

        self.button_vertical_layout = QVBoxLayout(main_form)

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.button_vertical_layout.addWidget(self.home_button, 0, Qt.AlignHCenter)
        self.button_vertical_layout.addItem(self.spacer_10_v)
        self.button_vertical_layout.addWidget(self.news_button, 0, Qt.AlignHCenter)
        self.button_vertical_layout.addItem(self.spacer_8_v)
        self.button_vertical_layout.addWidget(self.collection_button, 0, Qt.AlignHCenter)
        self.button_vertical_layout.addItem(self.spacer_8_v)
        self.button_vertical_layout.addWidget(self.planning_button, 0, Qt.AlignHCenter)
        self.button_vertical_layout.addItem(self.spacer_8_v)
        self.button_vertical_layout.addWidget(self.search_button, 0, Qt.AlignHCenter)
        self.button_vertical_layout.addItem(self.spacer_8_v)
        self.button_vertical_layout.addWidget(self.panier_button, 0, Qt.AlignHCenter)
        self.button_vertical_layout.addItem(self.spacer_buttom)
        self.button_vertical_layout.addWidget(self.account_button, 0, Qt.AlignHCenter )

        self.main_layout.addLayout(self.button_vertical_layout)
        self.main_layout.addWidget(self.line)

    def __update_init_home_button(self):
        self.home_button.setMinimumSize(SIZE_BUTTON_MENU)
        self.home_button.setMaximumSize(SIZE_BUTTON_MENU)
        self.home_button.setAutoFillBackground(False)
        self.home_button.setIcon(ICON_HOME)
        self.home_button.setIconSize(QSize(46, 46))
        self.home_button.setCheckable(False)
        self.home_button.setAutoDefault(False)

    def __update_init_news_button(self):
        self.news_button.setMinimumSize(SIZE_BUTTON_MENU)
        self.news_button.setMaximumSize(SIZE_BUTTON_MENU)
        self.news_button.setAutoFillBackground(False)
        self.news_button.setIcon(ICON_NEWS)
        self.news_button.setIconSize(SIZE_ICON_BUTTON_MENU)

    def __update_collection_button(self):
        self.collection_button.setMinimumSize(SIZE_BUTTON_MENU)
        self.collection_button.setMaximumSize(SIZE_BUTTON_MENU)
        self.collection_button.setAutoFillBackground(False)
        self.collection_button.setIcon(ICON_COLLECTION)
        self.collection_button.setIconSize(SIZE_ICON_BUTTON_MENU)

    def __update_planning_button(self):
        self.planning_button.setMinimumSize(SIZE_BUTTON_MENU)
        self.planning_button.setMaximumSize(SIZE_BUTTON_MENU)
        self.planning_button.setAutoFillBackground(False)
        self.planning_button.setIcon(ICON_PLANNING)
        self.planning_button.setIconSize(SIZE_ICON_BUTTON_MENU)

    def __update_search_button(self):
        self.search_button.setMinimumSize(SIZE_BUTTON_MENU)
        self.search_button.setMaximumSize(SIZE_BUTTON_MENU)
        self.search_button.setAutoFillBackground(False)
        self.search_button.setIcon(ICON_SEARCH)
        self.search_button.setIconSize(SIZE_ICON_BUTTON_MENU)

    def __update_panier_button(self):
        self.panier_button.setMinimumSize(SIZE_BUTTON_MENU)
        self.panier_button.setMaximumSize(SIZE_BUTTON_MENU)
        self.panier_button.setAutoFillBackground(False)
        self.panier_button.setIcon(ICON_PANIER)
        self.panier_button.setIconSize(SIZE_ICON_BUTTON_MENU)

    def __update_account_button(self):

        self.account_button.setMinimumSize(SIZE_BUTTON_MENU)
        self.account_button.setMaximumSize(SIZE_BUTTON_MENU)
        self.account_button.setIcon(ICON_ACCOUNT)
        self.account_button.setIconSize(SIZE_ICON_BUTTON_MENU)