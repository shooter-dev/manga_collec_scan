import sys
import asyncio
from PyQt5 import QtWidgets, QtCore
from bleak import BleakScanner, BleakClient

class BluetoothWorker(QtCore.QThread):
    devices_found = QtCore.pyqtSignal(list)

    async def scan(self):
        """ Fonction asynchrone pour scanner les périphériques Bluetooth. """
        devices = await BleakScanner.discover()
        self.devices_found.emit(devices)

    def run(self):
        """ Exécution de la boucle événementielle asyncio pour le scan. """
        asyncio.run(self.scan())


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

        # Gestionnaire de périphériques Bluetooth
        self.devices = []
        self.bluetooth_worker = BluetoothWorker()
        self.bluetooth_worker.devices_found.connect(self.display_devices)

    def scan_devices(self):
        """ Démarrer le scan Bluetooth avec QThread. """
        self.devices_list.clear()
        self.bluetooth_worker.start()

    def display_devices(self, devices):
        """ Affiche les périphériques trouvés dans la liste. """
        self.devices = devices
        for device in devices:
            self.devices_list.addItem(f"{device.name} - {device.address}")

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
                asyncio.create_task(self.connect_to_device_async(address))
        else:
            QtWidgets.QMessageBox.warning(self, "Aucun périphérique sélectionné", "Veuillez sélectionner un périphérique pour vous connecter.")


def main():
    app = QtWidgets.QApplication(sys.argv)
    dashboard = BluetoothDashboard()
    dashboard.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
