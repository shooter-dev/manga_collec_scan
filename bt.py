import sys
import asyncio
from PyQt5 import QtWidgets, QtCore
from bleak import BleakScanner, BleakClient

class BluetoothDashboard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Configurer l'interface utilisateur
        self.setWindowTitle("Tableau de Bord Bluetooth")
        self.resize(500, 300)

        # Layout principal
        self.layout = QtWidgets.QVBoxLayout(self)

        # Bouton pour scanner les périphériques
        self.scan_button = QtWidgets.QPushButton("Scanner les périphériques")
        self.scan_button.clicked.connect(self.scan_devices)
        self.layout.addWidget(self.scan_button)

        # Liste pour afficher les périphériques trouvés
        self.devices_list = QtWidgets.QListWidget()
        self.layout.addWidget(self.devices_list)

        # Bouton pour se connecter
        self.connect_button = QtWidgets.QPushButton("Se connecter")
        self.connect_button.clicked.connect(self.connect_to_device)
        self.layout.addWidget(self.connect_button)

        # Gestionnaire de périphérique Bluetooth
        self.devices = []

    async def scan_devices_async(self):
        """ Fonction asynchrone pour scanner les périphériques Bluetooth. """
        self.devices_list.clear()
        self.devices = await BleakScanner.discover()
        for device in self.devices:
            self.devices_list.addItem(f"{device.name} - {device.address}")

    def scan_devices(self):
        """ Démarrer le scan Bluetooth. """
        loop = asyncio.get_event_loop()
        loop.create_task(self.scan_devices_async())

    async def connect_to_device_async(self, address):
        """ Fonction asynchrone pour se connecter à un périphérique Bluetooth. """
        try:
            async with BleakClient(address) as client:
                if await client.is_connected():
                    QtWidgets.QMessageBox.information(self, "Connexion réussie", f"Connecté à {address}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erreur de connexion", str(e))

    def connect_to_device(self):
        """ Se connecter au périphérique sélectionné dans la liste. """
        selected_item = self.devices_list.currentItem()
        if selected_item:
            selected_device_info = selected_item.text().split(" - ")
            if len(selected_device_info) == 2:
                address = selected_device_info[1]
                loop = asyncio.get_event_loop()
                loop.create_task(self.connect_to_device_async(address))
        else:
            QtWidgets.QMessageBox.warning(self, "Aucun périphérique sélectionné", "Veuillez sélectionner un périphérique pour vous connecter.")

def main():
    app = QtWidgets.QApplication(sys.argv)
    dashboard = BluetoothDashboard()
    dashboard.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
