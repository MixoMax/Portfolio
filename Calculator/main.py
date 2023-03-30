import sys
from requirements import req
req()
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
import math



class Calculator(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Calculator")
        width, height = 300, 200
        self.setFixedSize(width, height)

        central_widget = QWidget(self)
        central_widget.setStyleSheet("background-color: #7B8794;")
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.result_edit = QLineEdit()
        self.result_edit.setAlignment(Qt.AlignLeft)
        self.result_edit.setStyleSheet("font-size: 20px; border-radius: 5px;")
        
        self.Enter_button = QPushButton("Enter")
        self.Enter_button.clicked.connect(lambda: self.button_clicked("="))
        self.Enter_button.setFixedSize(width//4, width//8)
        self.Enter_button.setStyleSheet("font-size: 20px; border-radius: 5px; background-color: #e0e0e0;")
        
        self.vbox = QGridLayout()
        
        self.vbox.addWidget(self.result_edit, 0, 0)
        self.vbox.addWidget(self.Enter_button, 0, 1)
        
        layout.addLayout(self.vbox)

        buttons_layout = QGridLayout()

        # create buttons for numbers and operations with their positions (row, column)
        button_dict = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "+": (0, 3),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "-": (1, 3),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "*": (2, 3),
            "0": (3, 0),
            ".": (3, 1),
            "C": (3, 2),
            "/": (3, 3)
        }

        for text, pos in button_dict.items():
            self.create_button(text, *pos, buttons_layout)

        layout.addLayout(buttons_layout)


        self.keyPressEvent = self.handle_key_press

        self.history = []

    def create_button(self , text: str, row: int, col: int, layout) -> None:
        button = QPushButton(text)
        if text in "0123456789.":
            button.setStyleSheet("font-size: 20px; font-weight: bold; border-radius: 5px; background-color: #e0e0e0;")
        else:
            button.setStyleSheet("font-size: 20px; font-weight: bold; border-radius: 5px; background-color: #e0e0e0;")
        button.clicked.connect(lambda: self.button_clicked(text))
        layout.addWidget(button, row, col)

    def button_clicked(self, text: str) -> None:
        if text == "C":
            self.result_edit.setText("")
        elif text in "+-*/":
            # add the operator to the result edit
            self.result_edit.setText(self.result_edit.text() + text)
        elif text == "=":
            # evaluate the expression and show the result
            try:
                result_text = self.result_edit.text()

                replacements = {
                    "÷": "/",
                    "x": "*",
                    "√": "math.sqrt",
                    "sqrt": "math.sqrt",
                    "sin": "math.sin",
                    "cos": "math.cos",
                    "tan": "math.tan",
                    "log": "math.log",
                    "ln": "math.log",
                    "e": "math.e",
                    "pi": "math.pi",
                    "π": "math.pi",
                    "e": "*10**",
                    "{": "(",
                    "}": ")",
                    "[": "(",
                    "]": ")",
                    "over": "/",
                    "cdot": "*",
                    "times": "*",
                    "div": "/",
                    ",": ".",
                    "math.math": "math",
                }

                for key, value in replacements.items():
                    result_text = result_text.replace(key, value)
                
                self.history.append(result_text)
                if len(self.history) > 100:
                    self.history.pop(0)
                

                blocked_expressions = ["import", "__", "lambda", "os", "sys", "subprocess", "exec", "eval", "open"]
                for expression in blocked_expressions:
                    if expression in result_text:
                        self.result_edit.setText("Error")
                        return None
                else:
                    result = eval(result_text)
                    
                    # if the result is a float and has no decimal places, convert it to an integer
                    if math.floor(result) == result:
                        result = int(result)
                    
                    # remove floating point errors (e.g. 0.1 + 0.2 = 0.30000000000000004) -> 0.3
                    result = "".join(str(result).split("000000000000000")[0])
                    if result[-1] == ".":
                        result = result[:-1]
                    self.result_edit.setText(str(result))
            except:
                self.result_edit.setText("Error")
        
        elif text == "up":
            self.result_edit.setText(self.history[-1]) if len(self.history) > 0 else ""
            self.history.pop(-1) if len(self.history) > 0 else None
        
        else:
            if self.result_edit.text() == "Error":
                self.result_edit.setText("")
            # add the number to the result edit
            self.result_edit.setText(self.result_edit.text() + text)

    def handle_key_press(self, event) -> None:
        key = event.key()
        

        key_dict = {
            16777235: "up", # up arrow key value on windows
        }


        if key in  range(0,9):
            self.button_clicked(key)
        elif key == Qt.Key_Plus:
            self.button_clicked("+")
        elif key == Qt.Key_Minus:
            self.button_clicked("-")
        elif key == Qt.Key_Asterisk:
            self.button_clicked("*")
        elif key == Qt.Key_Slash:
            self.button_clicked("/")
        elif key == Qt.Key_Period:
            self.button_clicked(".")
        elif key == Qt.Key_Enter or key == Qt.Key_Return:
            self.button_clicked("=")
        elif key == Qt.Key_Backspace:
            self.button_clicked("C")
        
        elif len(str(key)) < 2:
            self.button_clicked(str(key))
        
        elif key in key_dict:
            self.button_clicked(key_dict[key])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())