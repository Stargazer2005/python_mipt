from PyQt6 import QtWidgets
from calc_ui import Ui_Form


class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.is_answer = False

        self.numbers = [
            self.ui.pushButton_0,
            self.ui.pushButton_1,
            self.ui.pushButton_2,
            self.ui.pushButton_3,
            self.ui.pushButton_4,
            self.ui.pushButton_5,
            self.ui.pushButton_6,
            self.ui.pushButton_7,
            self.ui.pushButton_8,
            self.ui.pushButton_9,
        ]

        self.ops = [
            self.ui.pushButton_plus,
            self.ui.pushButton_minus,
            self.ui.pushButton_mul,
            self.ui.pushButton_div,
            self.ui.pushButton_pow,
            self.ui.pushButton_percent,
        ]

        self.ops_with_number = [
            self.ui.pushButton_rev,
            self.ui.pushButton_sqr,
            self.ui.pushButton_sqrt,
        ]

        for i in range(10):
            self.connect_number(self.numbers[i], str(i))

        for i, op in enumerate("+-*/^%"):
            self.connect_op(self.ops[i], op)

        for i, op in enumerate(
            [
                "1/",
                "^2",
                "^(1/2)",
            ]
        ):
            self.connect_op_with_num(self.ops_with_number[i], op)

        self.ui.pushButton_C.clicked.connect(self.connect_C)
        self.ui.pushButton_del.clicked.connect(self.connect_del)
        self.ui.pushButton_eq.clicked.connect(self.calculate)
        self.ui.pushButton_dot.clicked.connect(self.connect_dot)
        self.ui.pushButton_neg.clicked.connect(self.connect_neg)

    # Кнопка, отвечающая за +/-
    def connect_neg(self):
        self.check_answer()
        text = self.ui.lineEdit.displayText()
        if text and text[-1] in "0123456789":
            i = len(text) - 1
            while i != -1:
                if text[i] in "+-*/)%^":
                    break
                i -= 1
            self.ui.lineEdit.setText(text[: i + 1] + "(-" + text[i + 1 :] + ")")

    # Кнопка, отвечающая за .
    def connect_dot(self):
        self.check_answer()
        text = self.ui.lineEdit.displayText()
        if text and text[-1] in "0123456789":
            i = len(text) - 1
            flag = True
            while i != 0:
                if text[i] in "+-*/)%^":
                    break
                elif text[i] == ".":
                    flag = False
                    break
                i -= 1
            if flag:
                self.ui.lineEdit.setText(text + ".")

    def connect_op_with_num(self, button, op):
        button.clicked.connect(lambda: self.add_op_with_num(op))

    def connect_op(self, button, op):
        button.clicked.connect(lambda: self.add_op(op))

    # Кнопки, отвечающие за (x^2, x^(1/2), 1/x)
    def add_op_with_num(self, op):
        self.check_answer()
        text = self.ui.lineEdit.displayText()
        if op == "1/":
            for s in "+-/*^%":
                if s in text:
                    i = len(text) - 1
                    while text[i] not in "+-/*^":
                        i -= 1
                    self.ui.lineEdit.setText(text[: i + 1] + "1/" + text[i + 1 :])
                    break
            else:
                self.ui.lineEdit.setText(op + text)
        else:
            if text and text[-1] not in "+-*/%.^":
                self.ui.lineEdit.setText(text + op)

    # Кнопка =
    def calculate(self):
        text = self.ui.lineEdit.displayText().replace("^", "**")
        if text != "" and text[-1] not in "+-*/%.^":
            self.is_answer = True
            try:
                self.ui.lineEdit.setText(str(eval(text)))
            except ZeroDivisionError:
                self.ui.lineEdit.setText("You can't divide by 0!")
            except:
                self.ui.lineEdit.setText("Incorrect expression!")

    # Кнопка C
    def connect_C(self):
        self.ui.lineEdit.clear()

    # Кнопка del
    def connect_del(self):
        self.check_answer()
        text = self.ui.lineEdit.displayText()
        self.ui.lineEdit.setText(text[:-1])

    # Кнопки, отвечающие за (+, -, *, /, ^, %)
    def add_op(self, op):
        self.check_answer()
        text = self.ui.lineEdit.displayText()
        if text and text[-1] not in "+-*/%^":
            self.ui.lineEdit.setText(text + op)

    def connect_number(self, button, number):
        button.clicked.connect(lambda: self.add_number(number))

    # Кнопки, отвечающие за цифры
    def add_number(self, number):
        self.check_answer()
        text = self.ui.lineEdit.displayText()
        if (len(text) == 1 and text[-1] == "0") or (
            len(text) >= 2 and text[-1] == "0" and text[-2] not in "0123456789."
        ):
            self.ui.lineEdit.setText(text + "." + number)
        else:
            self.ui.lineEdit.setText(text + number)

    # Проверка на то, что ответ получен
    def check_answer(self):
        if self.is_answer:
            self.ui.lineEdit.clear()
            self.is_answer = False


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.exec()
