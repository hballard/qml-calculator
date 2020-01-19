from typing import List, Optional, Union


def convert_string_to_num(s: str) -> Union[int, float]:
    try:
        return int(s)
    except ValueError:
        return float(s)


class CalculatorController:
    current_value: Optional[str] = None
    current_expression: List = []
    clear_all: bool = False

    def on_digit_click(self, digit: str) -> str:
        if self.current_value:
            self.current_value = self.current_value + digit
        else:
            self.current_value = digit
        return self.current_value

    def on_decimal_click(self) -> str:
        if self.current_value:
            if "." not in self.current_value:
                self.current_value = self.current_value + "."
        else:
            self.current_value = "."
        return self.current_value

    def on_percent_click(self) -> Optional[str]:
        if self.current_value:
            num = convert_string_to_num(self.current_value)
            self.current_value = str(num / 100)
            return self.current_value
        return None

    def on_change_sign_click(self) -> Optional[str]:
        if self.current_value:
            num = convert_string_to_num(self.current_value)
            self.current_value = str(-num)
            return self.current_value
        return None

    def on_clear_click(self) -> None:
        if self.current_value:
            self.current_value = None
            self.clear_all = True
        elif self.clear_all:
            self.current_expression = []
            self.current_value = None
            self.clear_all = False
        else:
            self.clear_all = False

    def on_operator_click(self, operator: str) -> Optional[str]:
        if not self.current_value and self.current_expression:
            self.current_expression.pop()
            self.current_expression.append(operator)
            return None
        elif self.current_value and not self.current_expression:
            self.current_expression.append(self.current_value)
            self.current_expression.append(operator)
            self.current_value = None
            return None
        elif self.current_value and self.current_expression:
            self.current_expression.append(self.current_value)
            if operator in ["*", "/"] and self.current_expression[-2] in ["+", "-"]:
                pass
            else:
                try:
                    self.current_value = str(eval("".join(self.current_expression)))
                except ZeroDivisionError:
                    self.current_value = "Not a Number"
                return self.current_value
            self.current_expression.append(operator)
            self.current_value = None
            return None
        else:
            return None

    def on_equals_click(self) -> Optional[str]:
        if self.current_value:
            self.current_expression.append(self.current_value)
        elif self.current_expression:
            self.current_expression.append(self.current_expression[0])
        else:
            return None
        try:
            self.current_value = str(eval("".join(self.current_expression)))
        except ZeroDivisionError:
            self.current_value = "Not a Number"
        self.current_expression = []
        return self.current_value
