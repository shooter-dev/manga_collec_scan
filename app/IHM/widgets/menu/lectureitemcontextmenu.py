from typing import Any

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QTransform, QRegion, QPainterPath
from PyQt5.QtWidgets import QWidget, QAction, QMenu

from app.const import ICON_MENUE_VALIDATE, ICON_MENUE_PAUSE, FONT_17, STYLE_COLOR_TEXT, \
    STYLE_COLOR_BACKGROUND, STYLE_COLOR_STATE_HOVER, STYLE_COLOR_BORDER, STYLE_COLOR_STATE_PRESS


class LectureItemContextMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.create_widgets()
        self.modify_widgets()

    def create_widgets(self) -> Any:
        self.setObjectName(u"menu_lecture_item")

        self.action_lu = QAction(ICON_MENUE_VALIDATE, "Marquer comme lu", self)
        self.action_pause = QAction(ICON_MENUE_PAUSE, "Mettre en pause", self)

    def modify_widgets(self) -> Any:

        self.action_lu.triggered.connect(self.on_action_lu_triggered)
        self.action_pause.triggered.connect(self.on_action_pause_triggered)

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

        self.addAction(self.action_lu)
        self.addAction(self.action_pause)

    def on_action_lu_triggered(self):
        print(f"click click ")

    def on_action_pause_triggered(self):
        print(f"click click ")

    def resizeEvent(self, event):
        path = QPainterPath()
        # the rectangle must be translated and adjusted by 1 pixel in order to
        # correctly map the rounded shape
        rect = QRectF(self.rect()).adjusted(.5, .5, -1.5, -1.5)
        path.addRoundedRect(rect, 12, 12)
        # QRegion is bitmap based, so the returned QPolygonF (which uses float
        # values must be transformed to an integer based QPolygon
        region = QRegion(path.toFillPolygon(QTransform()).toPolygon())
        self.setMask(region)