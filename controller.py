from typing import List, Optional, Union

from PySide2.QtCore import QObject, Property, Signal, Slot


def convert_string_to_num(s: str) -> Union[int, float]:
    try:
        return int(s)
    except ValueError:
        return float(s)


class CalculatorController(QObject):
    current_value: str = ""
    current_expression: List = []
    clear_all: bool = False
    _display: str = ""
    display_changed = Signal()
    _clear_button_text: str = "AC"
    clear_button_text_changed = Signal()

    def __init__(self):
        super().__init__()

    def get_display(self):
        return self._display

    def set_display(self, value):
        self._display = value
        self.display_changed.emit()

    display = Property(str, get_display, set_display, notify=display_changed)

    def get_clear_button_text(self):
        return self._clear_button_text

    def set_clear_button_text(self, value):
        self._clear_button_text = value
        self.clear_button_text_changed.emit()

    clear_button_text = Property(
        str,
        get_clear_button_text,
        set_clear_button_text,
        notify=clear_button_text_changed,
    )

    @Slot(str)
    def on_digit_click(self, digit: str):
        if not self.current_value:
            self.clear_button_text = "C"
        self.current_value = self.current_value + digit
        self.display = self.current_value

    @Slot()
    def on_decimal_click(self) -> None:
        if "." not in self.current_value:
            self.current_value = self.current_value + "."
        self.display = self.current_value

    @Slot()
    def on_percent_click(self) -> None:
        if self.current_value:
            num = convert_string_to_num(self.current_value)
            self.current_value = str(num / 100)
        self.display = self.current_value

    @Slot()
    def on_change_sign_click(self) -> None:
        if self.current_value:
            num = convert_string_to_num(self.current_value)
            self.current_value = str(-num)
        self.display = self.current_value

    @Slot()
    def on_clear_click(self) -> None:
        if self.current_value:
            self.current_value = ""
            self.clear_all = True
        elif self.clear_all:
            self.current_expression = []
            self.current_value = ""
            self.clear_all = False
        else:
            self.clear_all = False
        self.display = ""
        self.clear_button_text = "AC"

    @Slot(str)
    def on_operator_click(self, operator: str) -> None:
        if not self.current_value and self.current_expression:
            self.current_expression.pop()
            self.current_expression.append(operator)
        elif self.current_value and not self.current_expression:
            self.current_expression.append(self.current_value)
            self.current_expression.append(operator)
            self.current_value = ""
        elif self.current_value and self.current_expression:
            self.current_expression.append(self.current_value)
            if operator in ["*", "/"] and self.current_expression[-2] in ["+", "-"]:
                pass
            else:
                try:
                    self.current_value = str(eval("".join(self.current_expression)))
                except ZeroDivisionError:
                    self.current_value = "Not a Number"
                self.display = self.current_value
            self.current_expression.append(operator)
            self.current_value = ""

    @Slot()
    def on_equals_click(self) -> None:
        if self.current_value:
            self.current_expression.append(self.current_value)
        elif self.current_expression:
            self.current_expression.append(self.current_expression[0])
        try:
            self.current_value = str(eval("".join(self.current_expression)))
        except ZeroDivisionError:
            self.current_value = "Not a Number"
        self.current_expression = []
        self.display = self.current_value
