pragma Singleton
import QtQuick 2.10

QtObject {
    readonly property int width: 560
    readonly property int height: 347
    readonly property real buttonWidth: 112
    readonly property real buttonHeight: 71.2

    readonly property color primaryColor: "darkgrey"
    readonly property color secondaryColor: "grey"
    readonly property color accentColor: "orange"
    readonly property color accentColorDark: "#d9d8d8"
    readonly property color textColor: "white"

    readonly property FontLoader mySystemFont: FontLoader {
        name: "Helvetica"
    }
    /* Edit this comment to add your custom font */
    /* readonly property FontLoader myCustomFont: FontLoader { source: "MyCustomFont.ttf" } */
    readonly property font font: Qt.font({
                                             "family": mySystemFont.name,
                                             "pixelSize": Qt.application.font.pixelSize
                                         })
    readonly property font largeFont: Qt.font({
                                                  "family": mySystemFont.name,
                                                  "pixelSize": Qt.application.font.pixelSize * 1.6
                                              })
}
