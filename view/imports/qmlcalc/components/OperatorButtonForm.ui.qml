import QtQuick 2.12
import qmlcalc 1.0

InputButton {
    id: root
    color: Constants.accentColor

    Connections {
        target: root.mouseArea
        onPressed: root.state = "press"
    }
    states: [
        State {
            name: "norm"
        },
        State {
            name: "press"

            PropertyChanges {
                target: root
                color: Qt.darker(Constants.accentColor, 1.2)
            }
        }
    ]
}

/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
