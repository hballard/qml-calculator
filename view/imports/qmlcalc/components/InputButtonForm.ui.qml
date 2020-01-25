import QtQuick 2.12
import qmlcalc 1.0

Rectangle {
    id: root
    implicitWidth: Constants.buttonWidth
    implicitHeight: Constants.buttonHeight
    border.color: Constants.secondaryColor
    color: Constants.primaryColor
    property alias mouseArea: mouseArea01
    property alias textColor: text01.color
    property alias text: text01.text
    signal clicked

    Text {
        id: text01
        color: 'white'
        text: qsTr("Text")
        anchors.fill: parent
        font.pointSize: 30
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    MouseArea {
        id: mouseArea01
        clip: false
        anchors.fill: parent
        onPressed: root.state = "pressed"
        onReleased: root.state = "normal"
    }

    states: [
        State {
            name: "normal"
        },
        State {
            name: "pressed"

            PropertyChanges {
                target: root
                color: Qt.lighter(Constants.primaryColor, 1.2)
            }
        }
    ]
}
