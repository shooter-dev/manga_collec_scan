from typing import Any

from PyQt5.QtWidgets import QWidget, QLabel, QTabWidget, QVBoxLayout

from app.IHM.widgets.search_collection_header.search_collection_header import SearchCollectionHeader
from app.IHM.widgets.tab_collection.tab_collection import TabCollection
from app.const import STYLE_COLOR_STATE_HOVER, STYLE_COLOR_PRIMARY, FONT_16, STYLE_COLOR_BORDER, STYLE_COLOR_BACKGROUND
from app.lib.controller import Controller
from app.lib.interface_widget import InterfaceWidget


class UiCollectionPage(InterfaceWidget):

    def init(self, main_form: QWidget):
        main_form.setStyleSheet(f"""
            QTabWidget::pane {{
                border-top: 1px solid {STYLE_COLOR_BORDER};
                position: absolute;
                top: 1px;
            }}

            QTabWidget::tab-bar {{
                alignment: center;
            }}
            
            QTabBar::tab {{
                background-color: { STYLE_COLOR_BACKGROUND };
                border: none solid {STYLE_COLOR_BORDER};
                border-radius: 15px;
                width:115px;
                min-height: 30px;
                margin: 6px
            }}

            QTabBar::tab:hover {{
                background: {STYLE_COLOR_STATE_HOVER};
            }}

            QTabBar::tab:selected {{
                border-color: ;
                background-color: {STYLE_COLOR_PRIMARY};
            }}
        """)

    def create_widgets(self, main_form: QWidget) -> Any:
        self.header = SearchCollectionHeader(main_form)
        self.header.setObjectName("SearchHeader")

        self.tabWidget = QTabWidget(main_form)
        self.tabWidget.setObjectName(u"tabWidget")

        self.tab_pile_a_lire = QWidget(main_form) #TabPileALire()
        self.tab_pile_a_lire.setObjectName(u"tab_pile_a_lire")

        self.tab_collection = TabCollection(main_form)
        self.tab_collection.setObjectName(u"tab_collection")

        self.tab_completer = QWidget(main_form)
        self.tab_completer.setObjectName(u"tab_completer")

        self.tab_envies = QWidget(main_form)
        self.tab_envies.setObjectName(u"tab_envies")

        self.tab_prets = QWidget(main_form)
        self.tab_prets.setObjectName(u"tab_prets")

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.tabWidget.addTab(self.tab_pile_a_lire, u"PILE A LIRE")
        self.tabWidget.addTab(self.tab_collection, u"COLLECTION")
        self.tabWidget.addTab(self.tab_completer, u"CONPLETER")
        self.tabWidget.addTab(self.tab_envies, u"ENVIES")
        self.tabWidget.addTab(self.tab_prets, u"PRETS")
        self.tabWidget.setFont(FONT_16)

        self.tabWidget.setCurrentIndex(1)

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.addWidget(self.header)
        self.main_layout.addWidget(self.tabWidget)

    def setup_connections(self) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass