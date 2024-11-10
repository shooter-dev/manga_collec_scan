from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPainter, QColor, QFont, QRgba64
from PyQt5.QtWidgets import QStyledItemDelegate, QStyle


class SizeDelegateComboBoxPublisher(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)
        self.font_size = 16  # Taille de la police pour les éléments

    def paint(self, painter, option, index):
        # Personnalisation de l'élément de la liste
        painter.save()
        painter.setRenderHint(QPainter.Antialiasing)

        # Couleur d'arrière-plan personnalisée
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, QColor(QRgba64.fromRgba(0,0,0,1)))  # Couleur de l'élément sélectionné
        else:
            painter.fillRect(option.rect, QColor("#FFFFFF"))  # Couleur de l'élément non sélectionné

        # Définir une police personnalisée
        font = QFont("Helvetica", 17, QFont.Normal)
        painter.setFont(font)
        painter.setPen(QColor("#000000"))  # Couleur du texte
        painter.drawText(option.rect, Qt.AlignCenter, index.data())

        painter.restore()

    def sizeHint(self, option, index):
        # Taille personnalisée de l'élément
        return QSize(223, 44)