import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel, QComboBox
from PyQt5.QtBluetooth import QBluetoothDeviceDiscoveryAgent, QBluetoothSocket, QBluetoothAddress, QBluetoothDeviceInfo


class BluetoothApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recherche Bluetooth")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Sélectionnez un périphérique Bluetooth", self)
        self.layout.addWidget(self.info_label)

        self.device_list = QListWidget(self)
        self.layout.addWidget(self.device_list)

        self.connect_button = QPushButton("Se connecter", self)
        self.connect_button.setEnabled(False)
        self.layout.addWidget(self.connect_button)

        self.quit_button = QPushButton("Quitter", self)
        self.layout.addWidget(self.quit_button)

        self.device_selector = QComboBox(self)
        self.layout.addWidget(self.device_selector)

        # Initialisation de la recherche Bluetooth
        self.device_discovery = QBluetoothDeviceDiscoveryAgent()
        self.device_discovery.deviceDiscovered.connect(self.on_device_discovered)
        self.device_discovery.finished.connect(self.on_discovery_finished)

        self.connect_button.clicked.connect(self.connect_to_device)
        self.quit_button.clicked.connect(self.close)

        self.setLayout(self.layout)

        self.device_info = None  # Pour stocker l'information du périphérique sélectionné

    def start_device_search(self):
        """Démarre la recherche des périphériques Bluetooth."""
        self.device_list.clear()
        self.device_selector.clear()
        self.device_discovery.start()

    def on_device_discovered(self, device_info):
        """Appelé lors de la découverte d'un périphérique."""
        self.device_list.addItem(device_info.name())
        self.device_selector.addItem(device_info.name())
        self.device_info = device_info  # On garde la dernière information du périphérique

    def on_discovery_finished(self):
        """Appelé une fois la recherche terminée."""
        self.info_label.setText(f"{self.device_list.count()} périphériques trouvés")
        if self.device_list.count() > 0:
            self.connect_button.setEnabled(True)

    def connect_to_device(self):
        """Se connecter au périphérique sélectionné."""
        device_name = self.device_selector.currentText()
        if not device_name:
            return

        # Recherche de l'adresse Bluetooth en fonction du nom
        device_address = None
        for i in range(self.device_list.count()):
            if self.device_list.item(i).text() == device_name:
                device_info = self.device_discovery.discoveredDevices()[i]
                device_address = device_info.address()
                break

        if device_address:
            self.bluetooth_socket = QBluetoothSocket(QBluetoothSocket.RfcommSocket)
            self.bluetooth_socket.connectToService(QBluetoothAddress(device_address), 1)  # Port 1 par défaut
            self.bluetooth_socket.readyRead.connect(self.on_data_received)
            self.bluetooth_socket.error.connect(self.on_connection_error)
            self.info_label.setText(f"Connexion à {device_name} en cours...")

    def on_data_received(self):
        """Gestion des données reçues après la connexion."""
        data = self.bluetooth_socket.readAll()
        print(f"Reçu: {data.data().decode()}")

    def on_connection_error(self):
        """Gérer les erreurs de connexion."""
        self.info_label.setText("Erreur de connexion.")
        print("Erreur de connexion.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = BluetoothApp()
    window.show()

    window.start_device_search()  # Démarrer la recherche des périphériques Bluetooth dès le début

    sys.exit(app.exec_())
