import QtQuick 2.12
import qmlcalc 1.0
import qmlcalc.components 1.0

Item {
    id: root
    width: Constants.width
    height: Constants.height
    property alias equalsButton: equalsButton
    property alias plusButton: plusButton
    property alias decimalButton: decimalButton
    property alias zeroButton: zeroButton
    property alias percentButton: percentButton
    property alias minusButton: minusButton
    property alias threeButton: threeButton
    property alias twoButton: twoButton
    property alias oneButton: oneButton
    property alias signButton: signButton
    property alias multiplyButton: multiplyButton
    property alias sixButton: sixButton
    property alias fiveButton: fiveButton
    property alias fourButton: fourButton
    property alias clearButton: clearButton
    property alias divideButton: divideButton
    property alias nineButton: nineButton
    property alias eightButton: eightButton
    property alias sevenButton: sevenButton
    property alias display: display

    Column {
        id: column
        spacing: 0
        anchors.fill: parent

        Row {
            id: row4
            height: 63
            anchors.right: parent.right
            anchors.left: parent.left
            anchors.rightMargin: 0
            anchors.leftMargin: 0

            Display {
                id: display
            }
        }

        Row {
            id: row
            height: 71
            anchors.left: parent.left
            anchors.leftMargin: 0
            anchors.right: parent.right
            anchors.rightMargin: 0

            InputButton {
                id: sevenButton
                text: "7"
            }

            InputButton {
                id: eightButton
                text: "8"
            }

            InputButton {
                id: nineButton
                text: "9"
            }

            OperatorButton {
                id: divideButton
                text: "/"
            }

            OperatorButton {
                id: clearButton
                text: "AC"
            }
        }

        Row {
            id: row1
            height: 71
            spacing: 0
            anchors.right: parent.right
            anchors.left: parent.left
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            InputButton {
                id: fourButton
                text: "4"
            }

            InputButton {
                id: fiveButton
                text: "5"
            }

            InputButton {
                id: sixButton
                text: "6"
            }

            OperatorButton {
                id: multiplyButton
                text: "x"
            }

            OperatorButton {
                id: signButton
                text: "+/-"
            }
        }

        Row {
            id: row2
            height: 71
            spacing: 0
            anchors.right: parent.right
            anchors.left: parent.left
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            InputButton {
                id: oneButton
                text: "1"
            }

            InputButton {
                id: twoButton
                text: "2"
            }

            InputButton {
                id: threeButton
                text: "3"
            }

            OperatorButton {
                id: minusButton
                text: "-"
            }

            OperatorButton {
                id: percentButton
                text: "%"
            }
        }

        Row {
            id: row3
            height: 71
            spacing: 0
            anchors.right: parent.right
            anchors.left: parent.left
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            InputButton {
                id: zeroButton
                width: 224
                text: "0"
            }

            OperatorButton {
                id: decimalButton
                text: "."
            }

            OperatorButton {
                id: plusButton
                text: "+"
            }

            InputButton {
                id: equalsButton
                text: "="
                color: Qt.lighter(Constants.primaryColor, 1.3)
                textColor: Constants.secondaryColor
            }
        }
    }
}
