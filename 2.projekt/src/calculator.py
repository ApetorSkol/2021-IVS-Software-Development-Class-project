"""! @file calculator.py
@brief Main file using math library and gui for the calculator
@author xhnato00, xlanro00, xmacho12, xslivk03
"""

# Importing math library.
import math_library as mlib
from PyQt5 import QtWidgets, uic

# Copying lambda functions.
from functools import partial
import enum

# Importing class UiHelpWindow from HelpWindow.py for the openHelp function.
from HelpWindow import UiHelpWindow

# Importing path for use in ui.
from os import path
import sys

# After packing everything into one executable, we have to find the ui file.
bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
# Path to a ui file created in QT Creator"""
path_to_ui = path.abspath(path.join(bundle_dir, 'calculator.ui'))


class Workspace:
    """! Class containing methods working with finite state machine,
    computing operations and printing output to display.
    """

    class State(enum.Enum):
        """! Class where the states of the state machine are defined."""

        TAKING_FIRST = 1
        TAKING_SECOND = 2
        SHOWING_RESULT = 3

    def __init__(self, printFn):
        """! Define and initialize operands and operators.
        Define other variables.
        """

        self.state = self.State.TAKING_FIRST
        self.firstOperand = ''
        self.firstOperand = ''
        self.secondOperand = ''
        self.operator = ''
        self.printFn = printFn

        self.unaryMap = {
            'a': mlib.absolute,
            'sin': mlib.sine,
            'cos': mlib.cosine,
            'tg': mlib.tangent,
            '!': mlib.factorial,
        }

        self.binaryMap = {
            '+': (mlib.add, False),
            '-': (mlib.subtract, False),
            '*': (mlib.multiply, False),
            '/': (mlib.divide, False),
            'r': (mlib.root, True),
            '^': (mlib.exponentiate, False),
            'log': (mlib.logarithm, True),
        }

        self.operatorMap = {
            'r': '√',
            '/': '÷',
            '*': '×',
        }

        self.operandMap = {
            'π': round(mlib.PI, 6),
            'e': round(mlib.E, 6),
        }


    def clear(self):
        """! Clear operators and operands string."""

        self.operator = ''
        self.firstOperand = ''
        self.secondOperand = ''


    def readNew(self, symbol):
        """! Read input and process it, call functions compute and show.
        Using finite state machine principle.
        """

        binaryOperators = self.binaryMap.keys()
        unaryOperators = self.unaryMap.keys()

        if self.state == self.State.TAKING_FIRST:
            if symbol == '=':
                self.compute()

            elif symbol == '-' and self.firstOperand == '':
                self.firstOperand = symbol

            elif symbol == 'C':
                self.clear()

            elif symbol == 'DEL':
                if not self.operator == '':
                    self.operator = ''

                elif not self.firstOperand == '':
                    self.firstOperand = self.firstOperand[:-1]

            elif symbol in unaryOperators:
                if self.firstOperand == '':
                    pass

                else:
                    self.operator = symbol
                    self.compute()
                    self.state = self.State.SHOWING_RESULT

            elif symbol in binaryOperators:
                legit = True

                if self.firstOperand == '':
                    if symbol == 'r':
                        self.firstOperand = '2'
                    elif symbol == 'log':
                        self.firstOperand = '10'
                    elif symbol == '^':
                        self.firstOperand = 'e'
                    else:
                        legit = False

                if legit:
                    self.operator = symbol
                    self.state = self.State.TAKING_SECOND

            elif symbol in self.operandMap.keys() and not self.firstOperand == '':
                if self.firstOperand == '-':
                    self.firstOperand = str(self.firstOperand) + str(self.operandMap[symbol])
                else:
                    pass

            else:
                self.firstOperand = str(self.firstOperand) + str(symbol)

        elif self.state == self.State.TAKING_SECOND:
            if symbol == '=':
                if self.operator in binaryOperators and self.firstOperand == '':
                    if self.operator == 'log':
                        self.firstOperand = '10'
                    elif self.operator == 'r':
                        self.firstOperand = '2'
                self.compute()
                self.state = self.State.SHOWING_RESULT

            elif symbol == '-' and self.secondOperand == '':
                self.secondOperand = symbol

            elif symbol == 'C':
                self.clear()
                self.state = self.State.TAKING_FIRST

            elif symbol == 'DEL':
                if not self.secondOperand == '':
                    self.secondOperand = self.secondOperand[:-1]

                elif not self.operator == '':
                    self.operator = ''
                    self.state = self.State.TAKING_FIRST

                elif not self.firstOperand == '':
                    self.firstOperand = self.firstOperand[:-1]
                    self.state = self.State.TAKING_FIRST

            elif symbol in unaryOperators:
                pass

            elif symbol in binaryOperators:
                pass

            elif symbol in self.operandMap.keys() and not self.secondOperand == '':

                if self.secondOperand == '-':
                    self.secondOperand = str(self.secondOperand) + str(self.operandMap[symbol])

                else:
                    pass

            else:
                self.secondOperand = str(self.secondOperand) + str(symbol)

        elif self.state == self.State.SHOWING_RESULT:
            if symbol == '=':
                pass

            elif symbol == 'C':
                self.clear()
                self.state = self.State.TAKING_FIRST

            elif symbol == 'DEL':
                if not self.firstOperand == '':
                    self.firstOperand = self.firstOperand[:-1]
                self.state = self.State.TAKING_FIRST

            elif symbol in unaryOperators:
                self.operator = symbol
                self.compute()

            elif symbol in binaryOperators:
                self.operator = symbol
                self.state = self.State.TAKING_SECOND

            else:
                self.firstOperand = str(symbol)
                self.state = self.State.TAKING_FIRST

        else:
            raise Exception('Illegal state')

        self.show()


    def compute(self):
        """! Read the operator and call corresponding math library function
        """

        try:
            op0 = float(self.firstOperand)

            if self.operator in self.unaryMap.keys():
                fn = self.unaryMap[self.operator]
                operationResult = fn(op0)

            elif self.operator in self.binaryMap.keys():
                op1 = float(self.secondOperand)
                fn = self.binaryMap[self.operator][0]
                if self.binaryMap[self.operator][1]:
                    operationResult = fn(op1, op0)

                else:
                    operationResult = fn(op0, op1)

            elif self.operator == '':
                operationResult = op0

            else:
                raise Exception('Unknown operator')

            operationResult = round(operationResult, 6)

            if float(operationResult).is_integer():
                operationResult = int(operationResult)

            self.firstOperand = str(operationResult)
            self.secondOperand = ''
            self.operator = ''

        except Exception:
            self.clear()
            self.firstOperand = 'Error'


    def show(self):
        """! Display current state of the calculator using print function.
        """

        printedOperator = self.operator

        if printedOperator in self.operatorMap.keys():
            printedOperator = self.operatorMap[printedOperator]

        if self.firstOperand in self.operandMap.keys():
            self.firstOperand = str(self.operandMap[self.firstOperand])

        if self.secondOperand in self.operandMap.keys():
            self.secondOperand = str(self.operandMap[self.secondOperand])

        self.printFn(f'{self.firstOperand} {printedOperator} {self.secondOperand}')



class MainWindow(QtWidgets.QMainWindow):
    """! Class of the main window.
    Set keyboard shortcuts and actions.
    Show the main window.
    """

    def __init__(self):
        """! Load the layout from the UI file created in QT Creator.
        """
        super().__init__()

        uic.loadUi(path_to_ui, self)

        # Printing function setText is the argument of a constructor.
        self.workspace = Workspace(self.resultBox.setText)
        self.setupMenuBar()
        self.setShortcuts()
        self.setActions()
        self.show()


    def setupMenuBar(self):
        """! Make the top left corner menu.
        Bind shortcuts for opening tutorial and closing the application.
        """
        # Using shortcut F1.
        self.actionHelp.setShortcut('F1')
        self.actionHelp.triggered.connect(self.openHelp)

        # Using shortcut Ctrl+Q.
        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.triggered.connect(self.exitAplication)


    def exitAplication(self):
        """! Close the application.
        """
        QtWidgets.qApp.quit()


    def openHelp(self):
        """! Opening a new window with tutorial.
        """
        self.helpWindow = UiHelpWindow()
        self.helpWindow.show()


    def setShortcuts(self):
        """! Set shortcuts for different operators, operands.
        Use QShortcut to bind more keys to one button.
        """

        # Use tuples of buttons and set some extra shortcuts.
        extraShortcuts = [
            (self.pushButtonEvaluate, ['Enter', 'Return']),
            (self.pushButtonDecimalPoint, [',']),
            (self.pushButtonDelete, ['Delete', 'Backspace']),
            (self.pushButtonMultiply, ['*']),
            (self.pushButtonDivide, ['/']),
        ]

        for button, keys in extraShortcuts:
            for key in keys:
                shortcut = QtWidgets.QShortcut(key, button)
                shortcut.activated.connect(button.animateClick)

        # Bind all the buttons to their keys.
        buttons = self.findChildren(QtWidgets.QPushButton)

        # Removed shortcuts to avoid unwanted behaviour.
        noShortcuts = [
            self.pushButtonExponent,
            self.pushButtonRoot,
            self.pushButtonAbsolute,
            self.pushButtonSinus,
            self.pushButtonCosinus,
            self.pushButtonTangens,
            self.pushButtonClear,
            self.pushButtonDelete,
        ]

        for removedButton in noShortcuts:
            buttons.remove(removedButton)

        for button in buttons:
            shortcut = button.text()
            button.setShortcut(shortcut)


    def setActions(self):
        """! Bind keys to the buttons on the screen.
        Special buttons have one symbol displayed on calculator,
        but here are used with a different one.
        """
        buttons = self.findChildren(QtWidgets.QPushButton)

        specialButtons = [
            (self.pushButtonExponent, '^'),
            (self.pushButtonRoot, 'r'),
            (self.pushButtonDivide, '/'),
            (self.pushButtonMultiply, '*'),
            (self.pushButtonFactorial, '!'),
            (self.pushButtonAbsolute, 'a'),
        ]

        for button, symbol in specialButtons:
            buttons.remove(button)
            fnPartial = partial(lambda s: self.workspace.readNew(s), s=symbol)
            button.clicked.connect(fnPartial)

        for button in buttons:
            symbol = button.text()
            fnPartial = partial(lambda s: self.workspace.readNew(s), s=symbol)
            button.clicked.connect(fnPartial)


app = QtWidgets.QApplication([])
window = MainWindow()

app.exec_()
