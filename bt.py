import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QListWidget, QPushButton, QWidget
from PyQt5.QtBluetooth import QBluetoothDeviceDiscoveryAgent, QBluetoothSocket, QBluetoothAddress, QBluetoothDeviceInfo


class BluetoothApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialiser les variables
        self.found_devices = []  # Liste pour stocker les périphériques trouvés
        self.bluetooth_socket = None

        # Configuration de l'interface
        self.initUI()

        # Configuration de la découverte Bluetooth
        self.discovery_agent = QBluetoothDeviceDiscoveryAgent()
        self.discovery_agent.deviceDiscovered.connect(self.on_device_discovered)
        self.discovery_agent.finished.connect(self.on_discovery_finished)

        # Démarrer la découverte des périphériques Bluetooth
        self.discovery_agent.start()

    def initUI(self):
        """Initialisation de l'interface graphique."""
        self.setWindowTitle("Bluetooth Scanner")
        self.setGeometry(100, 100, 400, 300)

        # Création du widget principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Création du layout vertical
        layout = QVBoxLayout()

        # Liste des périphériques Bluetooth
        self.device_list = QListWidget()
        layout.addWidget(self.device_list)

        # Label d'information
        self.info_label = QLabel("Recherche des périphériques Bluetooth...", self)
        layout.addWidget(self.info_label)

        # Bouton de connexion
        self.connect_button = QPushButton("Se connecter", self)
        self.connect_button.clicked.connect(self.connect_to_device)
        layout.addWidget(self.connect_button)

        # Ajouter le layout au widget principal
        central_widget.setLayout(layout)

    def on_device_discovered(self, device_info: QBluetoothDeviceInfo):
        """Méthode appelée lors de la découverte d'un périphérique Bluetooth."""
        # Ajouter chaque périphérique découvert à la liste
        self.device_list.addItem(device_info.name())

    def on_discovery_finished(self):
        """Méthode appelée lorsque la découverte des périphériques est terminée."""
        self.info_label.setText(f"{self.device_list.count()} périphériques trouvés.")

    def connect_to_device(self):
        """Se connecter au périphérique sélectionné."""
        selected_device_name = self.device_list.currentItem().text()

        # Trouver l'adresse Bluetooth du périphérique sélectionné
        selected_device = None
        for device in self.found_devices:
            if device.name() == selected_device_name:
                selected_device = device
                break

        if selected_device:
            device_address = selected_device.address()

            # Créer un objet QBluetoothSocket pour la connexion RFCOMM
            self.bluetooth_socket = QBluetoothSocket(QBluetoothSocket.RfcommSocket)

            # Se connecter au périphérique via RFCOMM
            self.bluetooth_socket.connectToService(QBluetoothAddress(device_address), 1)  # Port 1 par défaut

            # Connecter les signaux aux slots
            self.bluetooth_socket.readyRead.connect(self.on_data_received)
            self.bluetooth_socket.error.connect(self.on_connection_error)

            self.info_label.setText(f"Connexion à {selected_device_name}...")

    def on_data_received(self):
        """Méthode appelée lorsqu'il y a des données reçues sur le socket."""
        data = self.bluetooth_socket.readAll()
        self.info_label.setText(f"Données reçues : {data}")

    def on_connection_error(self):
        """Méthode appelée en cas d'erreur lors de la connexion Bluetooth."""
        error = self.bluetooth_socket.errorString()
        self.info_label.setText(f"Erreur de connexion : {error}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    bt_app = BluetoothApp()
    bt_app.show()
    sys.exit(app.exec_())
