import QtQuick 2.12

MainForm {
    display.text: controller.display || '0'
    clearButton.text: controller.clear_button_text

    oneButton.mouseArea.onClicked: function () {
        controller.on_digit_click('1')
    }
    twoButton.mouseArea.onClicked: function () {
        controller.on_digit_click('2')
    }
    threeButton.mouseArea.onClicked: function () {
        controller.on_digit_click('3')
    }
    fourButton.mouseArea.onClicked: function () {
        controller.on_digit_click('4')
    }
    fiveButton.mouseArea.onClicked: function () {
        controller.on_digit_click('5')
    }
    sixButton.mouseArea.onClicked: function () {
        controller.on_digit_click('6')
    }
    sevenButton.mouseArea.onClicked: function () {
        controller.on_digit_click('7')
    }
    eightButton.mouseArea.onClicked: function () {
        controller.on_digit_click('8')
    }
    nineButton.mouseArea.onClicked: function () {
        controller.on_digit_click('9')
    }
    zeroButton.mouseArea.onClicked: function () {
        controller.on_digit_click('0')
    }
    divideButton.mouseArea.onClicked: function () {
        controller.on_operator_click('/')
    }
    multiplyButton.mouseArea.onClicked: function () {
        controller.on_operator_click('*')
    }
    plusButton.mouseArea.onClicked: function () {
        controller.on_operator_click('+')
    }
    minusButton.mouseArea.onClicked: function () {
        controller.on_operator_click('-')
    }
    percentButton.mouseArea.onClicked: function () {
        controller.on_percent_click()
    }
    signButton.mouseArea.onClicked: function () {
        controller.on_change_sign_click()
    }
    decimalButton.mouseArea.onClicked: function () {
        controller.on_decimal_click()
    }
    clearButton.mouseArea.onClicked: function () {
        controller.on_clear_click()
    }
    equalsButton.mouseArea.onClicked: function () {
        controller.on_equals_click()
    }
}




/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
