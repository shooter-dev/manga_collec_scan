from typing import Any
from PyQt5.QtWidgets import QWidget, QAction, QMenu

from app.const import ICON_MENUE_VALIDATE, ICON_MENUE_PAUSE, FONT_17, STYLE_COLOR_TEXT, \
    STYLE_COLOR_BACKGROUND, STYLE_COLOR_STATE_HOVER, STYLE_COLOR_BORDER, STYLE_COLOR_STATE_PRESS


class MenuVolumeItem(QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.create_widgets()
        self.modify_widgets()

    def create_widgets(self) -> Any:
        self.setObjectName(u"menu_lecture_item")

        self.action_add_collection = QAction(ICON_MENUE_VALIDATE, "Ajouter à la collection", self)
        self.action_suivre = QAction(ICON_MENUE_PAUSE, "Ne plus suivre", self)
        self.action_lu = QAction(ICON_MENUE_PAUSE, "Marquer comme lu", self)
        self.action_add_panier = QAction(ICON_MENUE_PAUSE, "Ajouter au panier", self)

    def modify_widgets(self) -> Any:

        self.action_add_collection.triggered.connect(self.on_action_add_collection_triggered)
        self.action_suivre.triggered.connect(self.on_action_suivre_triggered)
        self.action_lu.triggered.connect(self.on_action_lu_triggere)
        self.action_add_panier.triggered.connect(self.on_action_add_panier_triggered)
        self.action_add_panier.triggered.connect(self.on_action_add_panier_triggered)

        self.setStyleSheet(f"""
            
            QMenu {{
                background: {STYLE_COLOR_BACKGROUND};
                border: 1px solid {STYLE_COLOR_BORDER};
                border-radius: 12px;
            }}
            QMenu::item {{
                color: {STYLE_COLOR_TEXT};
                border: 1px solid {STYLE_COLOR_BORDER};
                padding-left:12px;
                padding-right:12px;
                height: 44px;
                width: 238;
            }}
            QMenu::item:selected {{
                color: {STYLE_COLOR_TEXT};
                background: {STYLE_COLOR_STATE_PRESS};
            }}
        """)
        self.setFont(FONT_17)

        self.addAction(self.action_add_collection)
        self.addAction(self.action_suivre)
        self.addAction(self.action_lu)
        self.addAction(self.action_add_panier)

    def on_action_add_collection_triggered(self):
        print(f"click add Collection ")

    def on_action_suivre_triggered(self):
        print(f"click suivre ")

    def on_action_lu_triggered(self):
        print(f"click ajouter comme lu ")

    def on_action_add_panier_triggered(self):
        print(f"click add panier ")