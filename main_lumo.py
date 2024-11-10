import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtCore import Qt

# Initialiser QApplication avec les arguments de ligne de commande
app = QApplication(sys.argv)

# Paramètres généraux de l'application
app.setApplicationName("Exemple PyQt5")
app.setApplicationVersion("1.0.0")
app.setOrganizationName("MonOrganisation")
app.setWindowIcon(QIcon("icon.png"))

# Configuration du style et de la palette
app.setStyle("Fusion")
palette = QPalette()
palette.setColor(QPalette.Window, QColor("lightgrey"))
app.setPalette(palette)

# Configuration de la fenêtre principale
window = QWidget()
window.setWindowTitle("Fenêtre Principale")
window.setGeometry(100, 100, 300, 200)

# Ajouter un label
layout = QVBoxLayout()
label = QLabel("Bienvenue dans mon application PyQt5 !")
layout.addWidget(label)
window.setLayout(layout)

# Afficher la fenêtre
window.show()

# Lancer la boucle d'événements de l'application
sys.exit(app.exec_())
