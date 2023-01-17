import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import QtCore


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.button0 = QPushButton('0', self)
        self.button1 = QPushButton('1', self)
        self.button2 = QPushButton('2', self)
        self.button3 = QPushButton('3', self)
        self.button4 = QPushButton('4', self)
        self.button5 = QPushButton('5', self)
        self.button6 = QPushButton('6', self)
        self.button7 = QPushButton('7', self)
        self.button8 = QPushButton('8', self)
        self.button9 = QPushButton('9', self)
        self.buttonPlus = QPushButton('+', self)
        self.buttonMinus = QPushButton('-', self)
        self.buttonEgal = QPushButton('=', self)
        self.buttonClearAll = QPushButton('CE', self)
        self.buttonClearOne = QPushButton('C', self)
        self.buttonMultiply = QPushButton('X', self)
        self.buttonDivision = QPushButton('/', self)
        self.buttonDot = QPushButton('.', self)

        self.resultLabel = QLabel(self)
        self.title = 'Calculator'
        self.left = 500
        self.top = 250
        self.width = 225
        self.height = 200
        self.labelText = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.resultLabel.move(10, 10)
        self.resultLabel.resize(180, 20)
        self.resultLabel.setStyleSheet("background-color: lightgrey")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setText(self.labelText)

        # Create a button in the window
        self.button0.move(10, 50)
        self.button0.resize(30, 30)

        self.button1.move(40, 50)
        self.button1.resize(30, 30)

        self.button2.move(70, 50)
        self.button2.resize(30, 30)

        self.button3.move(10, 80)
        self.button3.resize(30, 30)

        # Create a button in the window
        self.button4.move(40, 80)
        self.button4.resize(30, 30)

        self.button5.move(70, 80)
        self.button5.resize(30, 30)

        self.button6.move(10, 110)
        self.button6.resize(30, 30)

        self.button7.move(40, 110)
        self.button7.resize(30, 30)

        self.button8.move(70, 110)
        self.button8.resize(30, 30)

        self.button9.move(40, 140)
        self.button9.resize(30, 30)

        self.buttonPlus.move(130, 50)
        self.buttonPlus.resize(30, 30)

        self.buttonMinus.move(160, 50)
        self.buttonMinus.resize(30, 30)

        self.buttonEgal.move(70, 140)
        self.buttonEgal.resize(30, 30)
        self.show()

        self.buttonMultiply.move(130, 80)
        self.buttonMultiply.resize(30, 30)
        self.show()

        self.buttonDivision.move(160, 80)
        self.buttonDivision.resize(30, 30)
        self.show()

        self.buttonClearAll.move(160, 110)
        self.buttonClearAll.resize(30, 30)
        self.show()

        self.buttonClearOne.move(130, 110)
        self.buttonClearOne.resize(30, 30)
        self.show()

        self.buttonDot.move(10, 140)
        self.buttonDot.resize(30, 30)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
