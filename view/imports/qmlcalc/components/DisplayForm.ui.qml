import QtQuick 2.12
import qmlcalc 1.0

Rectangle {
    implicitWidth: Constants.width
    implicitHeight: 63
    color: Constants.secondaryColor
    property alias textSize: text01.font.pixelSize
    property alias textColor: text01.color
    property alias text: text01.text

    Text {
        id: text01
        color: Constants.textColor
        text: qsTr("Text")
        rightPadding: 12
        anchors.fill: parent
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignRight
        font.pixelSize: 30
    }
}
