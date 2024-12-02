import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 720
    height: 1280
    title: "ComboBox Example"

    // Couleur de fond
    color: "#f0f0f0"

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20

        Text {
            text: "Sélectionnez un item :"
            font.pixelSize: 24
            horizontalAlignment: Text.AlignHCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }

        ComboBox {
            id: comboBox
            width: 400
            font.pixelSize: 20
            model: [
                "Item 1", "Item 2", "Item 3", "Item 4", "Item 5",
                "Item 6", "Item 7", "Item 8", "Item 9", "Item 10",
                "Item 11", "Item 12", "Item 13", "Item 14", "Item 15",
                "Item 16", "Item 17", "Item 18", "Item 19", "Item 20",
                "Item 21", "Item 22", "Item 23", "Item 24", "Item 25",
                "Item 26", "Item 27", "Item 28", "Item 29", "Item 30"
            ]
        }

        Text {
            id: selectedText
            text: "Item sélectionné : " + comboBox.currentText
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }
}
