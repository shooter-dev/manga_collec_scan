import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QColor, QPainter
from PyQt5.QtCore import QTimer, Qt


# Fonction pour générer des informations Wi-Fi simulées
def generate_random_wifi_info():
    ssid = f"Network_{random.randint(1, 100)}"  # Nom du réseau Wi-Fi simulé
    signal_strength = random.randint(-100, -50)  # Force du signal (en dBm, plage correcte)
    band = random.choice(["2.4 GHz", "5 GHz", "6 GHz"])  # Bande de fréquence
    ip_address = f"192.168.{random.randint(0, 255)}.{random.randint(1, 255)}"  # Adresse IP simulée
    channel = random.randint(1, 11)  # Canal Wi-Fi
    return ssid, signal_strength, band, ip_address, channel

class SystemInfoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(160)  # Taille fixe pour le widget
        self.wifi_info = self.generate_wifi_info()  # Générer les informations Wi-Fi simulées

        # Timer pour mettre à jour les informations toutes les 5 secondes
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_system_info)
        self.timer.start(5000)

    def generate_wifi_info(self):
        ssid, signal_strength, band, ip_address, channel = generate_random_wifi_info()
        wifi_info = {
            "SSID": ssid,
            "Signal Strength (dBm)": signal_strength,
            "Band": band,
            "IP Address": ip_address,
            "Channel": channel,
        }
        return wifi_info

    def update_system_info(self):
        # Mettre à jour les informations Wi-Fi à chaque intervalle
        self.wifi_info = self.generate_wifi_info()
        self.update()  # Déclencher un redessin du widget

    def get_signal_icon(self, signal_strength):
        """Retourner une icône de signal en fonction de la force du signal"""
        if signal_strength >= -60:
            return 'signal_full.png'  # Force du signal forte
        elif -70 <= signal_strength < -60:
            return 'signal_good.png'  # Signal moyen
        elif -80 <= signal_strength < -70:
            return 'signal_weak.png'  # Signal faible
        else:
            return 'signal_empty.png'  # Pas de signal

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # Couleur de fond
        painter.setBrush(QColor(44, 44, 44))  # Gris foncé
        painter.drawRect(0, 0, self.width(), self.height())

        # Informations Wi-Fi affichées
        painter.setPen(QColor(255, 255, 255))  # Texte en blanc
        painter.setFont(QFont('Arial', 10))

        # Affichage des informations Wi-Fi simulées
        y_offset = 20
        for key, value in self.wifi_info.items():
            painter.drawText(10, y_offset, f"{key}: {value}")
            y_offset += 20  # Espacement entre chaque ligne

        # Affichage de l'icône du signal
        signal_icon = self.get_signal_icon(self.wifi_info["Signal Strength (dBm)"])
        pixmap = QPixmap(signal_icon)
        painter.drawPixmap(250, 50, pixmap)  # Placer l'icône de signal à une position spécifique

        painter.end()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simulated System Information Display')
        self.setGeometry(100, 100, 400, 200)

        # Créer un layout et un widget pour afficher les informations
        layout = QVBoxLayout()
        self.system_info_widget = SystemInfoWidget()
        layout.addWidget(self.system_info_widget)

        # Conteneur principal pour le layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
