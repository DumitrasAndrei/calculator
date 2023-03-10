import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QMessageBox
from PyQt5 import QtCore


# Cream clasa App care va contine componentele vizuale si metodele.
class App(QMainWindow):

    def __init__(self):
        super().__init__()

        # Definim componentele si continutul lor.
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

        # Definim label-ul unde o sa avem rezultatele.
        self.resultLabel = QLabel(self)

        # Definim dimensiunile ferestrei pentru calculator.
        self.title = 'Calculator'
        self.left = 500
        self.top = 250
        self.width = 225
        self.height = 200
        self.labelText = ""
        self.initUI()

    def initUI(self):
        # Definim interfata calculatorului dupa dimensiunile setate mai sus, unde o sa fie componentele.
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Definim locul componentelor si dimensiunea lor in fereastra.
        self.resultLabel.move(10, 10)
        self.resultLabel.resize(180, 20)
        self.resultLabel.setStyleSheet("background-color: lightgrey")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setText(self.labelText)

        # prin self.[denumire_componenta].clicked.connect(lambda:self.[denumire_metoda])
        # adaugam un 'event listener' pe componenta pentru apelarea metodelor corespunzatoare
        self.button0.move(10, 50)
        self.button0.resize(30, 30)
        self.button0.clicked.connect(lambda: self.setNumber(0))

        self.button1.move(40, 50)
        self.button1.resize(30, 30)
        self.button1.clicked.connect(lambda: self.setNumber(1))

        self.button2.move(70, 50)
        self.button2.resize(30, 30)
        self.button2.clicked.connect(lambda: self.setNumber(2))

        self.button3.move(10, 80)
        self.button3.resize(30, 30)
        self.button3.clicked.connect(lambda: self.setNumber(3))

        # Create a button in the window
        self.button4.move(40, 80)
        self.button4.resize(30, 30)
        self.button4.clicked.connect(lambda: self.setNumber(4))

        self.button5.move(70, 80)
        self.button5.resize(30, 30)
        self.button5.clicked.connect(lambda: self.setNumber(5))

        self.button6.move(10, 110)
        self.button6.resize(30, 30)
        self.button6.clicked.connect(lambda: self.setNumber(6))

        self.button7.move(40, 110)
        self.button7.resize(30, 30)
        self.button7.clicked.connect(lambda: self.setNumber(7))

        self.button8.move(70, 110)
        self.button8.resize(30, 30)
        self.button8.clicked.connect(lambda: self.setNumber(8))

        self.button9.move(40, 140)
        self.button9.resize(30, 30)
        self.button9.clicked.connect(lambda: self.setNumber(9))

        self.buttonPlus.move(130, 50)
        self.buttonPlus.resize(30, 30)
        self.buttonPlus.clicked.connect(lambda: self.setOperator("+"))

        self.buttonMinus.move(160, 50)
        self.buttonMinus.resize(30, 30)
        self.buttonMinus.clicked.connect(lambda: self.setOperator("-"))

        self.buttonEgal.move(70, 140)
        self.buttonEgal.resize(30, 30)
        self.buttonEgal.clicked.connect(lambda: self.resultOperation())
        self.show()

        self.buttonMultiply.move(130, 80)
        self.buttonMultiply.resize(30, 30)
        self.buttonMultiply.clicked.connect(lambda: self.setOperator("*"))
        self.show()

        self.buttonDivision.move(160, 80)
        self.buttonDivision.resize(30, 30)
        self.buttonDivision.clicked.connect(lambda: self.setOperator("/"))
        self.show()

        self.buttonClearAll.move(160, 110)
        self.buttonClearAll.resize(30, 30)
        self.buttonClearAll.clicked.connect(lambda: self.clearField())
        self.show()

        self.buttonClearOne.move(130, 110)
        self.buttonClearOne.resize(30, 30)
        self.buttonClearOne.clicked.connect(lambda: self.clearOne())
        self.show()

        self.buttonDot.move(10, 140)
        self.buttonDot.resize(30, 30)
        self.buttonDot.clicked.connect(lambda: self.setDot())
        self.show()

    @pyqtSlot()
    # metoda care se apeleaza la apasarea unei cifre
    # si ne adauga in variabila labelText cifra corespunzatoare
    def setNumber(self, nr):
        self.labelText += str(nr)
        self.resultLabel.setText(self.labelText)
        QApplication.processEvents()

    # metoda care se apeleaza la apasarea unui operator
    # si ne adauga in variabila labelText operatorul corespunzator
    def setOperator(self, operator):
        if not self.labelText == "" and not self.labelText[-1] in "*/%+-=. ":
            self.labelText += operator
            self.resultLabel.setText(self.labelText)
            QApplication.processEvents()

    # metoda care se apeleaza la apasarea butonului 'egal'
    # si ne afiseaza rezultatul operatiilor din labelText
    def resultOperation(self):
        print(self.labelText[-1])
        if self.labelText == "":
            return
        if self.labelText[-1] == "+" or self.labelText[-1] == "/" or self.labelText[-1] == "*" or self.labelText[
            -1] == '-' or self.labelText[-1] == "+-" \
                or self.labelText[-1] == "-+" or self.labelText[-1] == "Invalid operation":
            self.labelText = ""
            self.resultLabel.setText(self.labelText)
            QMessageBox.about(self, "Error", "Invalid operation")
            return
        result = str(eval(self.labelText))
        self.labelText = result
        self.resultLabel.setText(result)
        QApplication.processEvents()
        print(result)

    # metoda care se apeleaza la apasarea butonului 'CE'
    # aceasta metoda sterge tot continulul din labelText
    def clearField(self):
        self.labelText = ""
        self.resultLabel.setText(self.labelText)
        QApplication.processEvents()

    # metoda care se apeleaza la apasarea butonului 'C'
    # aceasta metoda sterge cate un caracter per click din labelText
    def clearOne(self):
        self.labelText = self.labelText[:-1]
        self.resultLabel.setText(self.labelText)
        QApplication.processEvents()

    # metoda care se apeleaza la apasarea butonului '.'
    # aceasta adauga '.' in variabila labelText
    def setDot(self):
        if self.labelText == "" or self.labelText[-1] in "%+-=. ":
            self.labelText = ""
            self.resultLabel.setText(self.labelText)
            QMessageBox.about(self, "Error", "Invalid operation")
            return
        self.labelText += '.'
        self.resultLabel.setText(self.labelText)
        QApplication.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
