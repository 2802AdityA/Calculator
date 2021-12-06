from re import S
from PySide6.QtCore import (QCoreApplication, QEvent, QLine, QMetaObject, QSize, Qt, QStringConverter)
from PySide6.QtGui import (QBrush, QColor, QFont, QKeyEvent)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView, QLabel, QLineEdit, QMainWindow,QPushButton, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import sys
import sympy as sym

x = sym.Symbol('x')

menu_window_style = """background-image: url("wallpaper.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;"""
menu_button_style = ("QPushButton{\n"
        "   background: transparent;\n"
        "   font: 87 40pt \"Arial Black\";\n"
        "   color: rgb(255, 255, 255);\n"
        "   \n"
        "   \n"
        "   border-radius: 35px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    color: rgb(255, 255, 255);\n"
        "    background: transparent;\n"
        "    border: 5px solid white\n"
        "}\n"
        "\n"
        "\n"
        "\n"
        "QPushButton:hover:!pressed\n"
        "{\n"
        "    background: transparent;\n"
        "    color: rgb(255,255,255);\n"
        "border: 0px solid white\n"
        "}\n"
        "\n"
        "")
DnI_buttons_style = ("QPushButton{\n"
         "   font: 87 20pt \"Arial Black\";\n"
         "   color: rgb(255, 255, 255);\n"
         "   background-color: rgb(0, 0, 0);\n"
         "   border-radius: 35px;\n"
         "}\n"
         "\n"
         "QPushButton:hover{\n"
         "    color: rgb(255, 255, 255);\n"
         "    background-color: rgb(26, 26, 26);\n"
         "    border: 5px solid white\n"
         "}\n"
         "\n"
         "\n"
         "\n"
         "QPushButton:hover:!pressed\n"
         "{\n"
         "    \n"
         "    background-color: rgb(61, 61, 61);\n"
         "    color: rgb(255,255,255);\n"
         "border: 0px solid white\n"
         "}\n"
         "\n"
         "")
Limits_buttons_style = ("QPushButton{\n"
    "   font: 87 28pt \"Arial Black\";\n"
    "   color: rgb(255, 255, 255);\n"
    "   background-color: rgb(0, 0, 0);\n"
    "   border-radius: 35px;\n"
    "}\n"
    "\n"
    "QPushButton:hover{\n"
    "    color: rgb(255, 255, 255);\n"
    "    background-color: rgb(26, 26, 26);\n"
    "    border: 5px solid white\n"
    "}\n"
    "\n"
    "\n"
    "\n"
    "QPushButton:hover:!pressed\n"
    "{\n"
    "    \n"
    "    background-color: rgb(61, 61, 61);\n"
    "    color: rgb(255,255,255);\n"
    "border: 0px solid white\n"
    "}\n"
    "\n"
    "")
Roots_buttons_style = ("QPushButton{\n"
    "   font: 87 32pt \"Arial Black\";\n"
    "   color: rgb(255, 255, 255);\n"
    "   background-color: rgb(0, 0, 0);\n"
    "   border-radius: 35px;\n"
    "}\n"
    "\n"
    "QPushButton:hover{\n"
    "    color: rgb(255, 255, 255);\n"
    "    background-color: rgb(26, 26, 26);\n"
    "    border: 5px solid white\n"
    "}\n"
    "\n"
    "\n"
    "\n"
    "QPushButton:hover:!pressed\n"
    "{\n"
    "    \n"
    "    background-color: rgb(61, 61, 61);\n"
    "    color: rgb(255,255,255);\n"
    "border: 0px solid white\n"
    "}\n"
    "\n"
    "")
History_buttons_style = ("QPushButton{\n"
                "   font: 87 28pt \"Arial Black\";\n"
                "   color: rgb(255, 255, 255);\n"
                "   background-color: rgb(0, 0, 0);\n"
                "   border-radius: 35px;\n"
                "}\n"
                "\n"
                "QPushButton:hover{\n"
                "    color: rgb(255, 255, 255);\n"
                "    background-color: rgb(26, 26, 26);\n"
                "    border: 5px solid white\n"
                "}\n"
                "\n"
                "\n"
                "\n"
                "QPushButton:hover:!pressed\n"
                "{\n"
                "    \n"
                "    background-color: rgb(61, 61, 61);\n"
                "    color: rgb(255,255,255);\n"
                "border: 0px solid white\n"
                "}\n"
                "\n"
                "")

class Ui_Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(menu_window_style)
        self.resize(800, 600)
        self.MainWidget = QWidget(self)
        self.VerticalLayout = QVBoxLayout(self.MainWidget)
        
        keys = [
            ("Differentiation and Integration", Qt.Key_A, self.show_dni),
            ("Limits", Qt.Key_B, self.show_limits),
            ("Roots", Qt.Key_C, self.show_roots),
            ("History", Qt.Key_D, self.show_history),
        ]
        for text, key, func in keys:
            Button = QPushButton(text=text, focusPolicy=Qt.NoFocus)
            Button.setProperty("__key__", key)
            Button.setStyleSheet(menu_button_style)
            
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(Button.sizePolicy().hasHeightForWidth())
            Button.setSizePolicy(sizePolicy)
            
            Button.clicked.connect(func)
            self.VerticalLayout.addWidget(Button)
        
        self.setCentralWidget(self.MainWidget)

        QMetaObject.connectSlotsByName(self)
    
    def show_dni(self):
        self.hide()
        self.ui_dni = Ui_DnI()
        self.ui_dni.show()
    
    def show_limits(self):
        self.hide()
        self.ui_limits = Ui_Limits()
        self.ui_limits.show()
    
    def show_roots(self):
        self.hide()
        self.ui_roots = Ui_Roots()
        self.ui_roots.show()
    
    def show_history(self):
        self.hide()
        self.ui_history = Ui_History()
        self.ui_history.show()
        
class Ui_DnI(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.resize(800, 800)
        
        
        self.InputWidget = QWidget(self)
        self.InputVerticalLayout = QVBoxLayout(self.InputWidget)
        
        self.InputLine = QLineEdit(self.InputWidget)
        self.OutputLine = QLineEdit(self.InputWidget)
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        
        self.InputLine.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        sizePolicy.setHeightForWidth(self.InputLine.sizePolicy().hasHeightForWidth())
        self.InputLine.setSizePolicy(sizePolicy)
        self.InputLine.setMinimumSize(QSize(0, 150))
        self.InputLine.setFont(font)
        self.InputLine.setStyleSheet("color: rgb(255, 255, 255);")
        self.InputLine.setText("")
        
        self.OutputLine.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        sizePolicy.setHeightForWidth(self.OutputLine.sizePolicy().hasHeightForWidth())
        self.OutputLine.setSizePolicy(sizePolicy)
        self.OutputLine.setMinimumSize(QSize(0, 150))
        self.OutputLine.setFont(font)
        self.OutputLine.setStyleSheet("color: rgb(255, 255, 255);")
        self.OutputLine.setText("")
        
        self.InputVerticalLayout.addWidget(self.InputLine)
        self.InputVerticalLayout.addWidget(self.OutputLine)
        
        self.MainVerticalLayout = QVBoxLayout(self)
        self.MainVerticalLayout.addWidget(self.InputWidget)
        
        self.KeypadWidget = QWidget(self)
        self.KeypadGridLayout = QGridLayout(self.KeypadWidget)
        
        keys = [
            ("Differentiate", Qt.Key_D, self.diff_clicked , 0, 0, 1, 3),
            ("Integrate", Qt.Key_I, self.inte_clicked , 0, 3, 1, 3),
            ("x", Qt.Key_X, self.on_clicked , 0, 6, 1, 1),
            ("sin()", Qt.Key_S, self.on_clicked , 1, 0, 1, 1),
            ("cos()", Qt.Key_C, self.on_clicked , 1, 1, 1, 1),
            ("tan()", Qt.Key_T, self.on_clicked , 1, 2, 1, 1),
            ("1", Qt.Key_1, self.on_clicked , 1, 3, 1, 1),
            ("2", Qt.Key_2, self.on_clicked , 1, 4, 1, 1),
            ("3", Qt.Key_3, self.on_clicked , 1, 5, 1, 1),
            ("+", Qt.Key_Plus, self.on_clicked , 1, 6, 1, 1),
            ("asin()", Qt.Key_L, self.on_clicked , 2, 0, 1, 1),
            ("acos()", Qt.Key_M, self.on_clicked , 2, 1, 1, 1),
            ("atan()", Qt.Key_N, self.on_clicked , 2, 2, 1, 1),
            ("4", Qt.Key_4, self.on_clicked , 2, 3, 1, 1),
            ("5", Qt.Key_5, self.on_clicked , 2, 4, 1, 1),
            ("6", Qt.Key_6, self.on_clicked , 2, 5, 1, 1),
            ("-", Qt.Key_Minus, self.on_clicked , 2, 6, 1, 1),
            ("e", Qt.Key_E, self.on_clicked , 3, 0, 1, 1),
            ("log()", Qt.Key_F, self.on_clicked , 3, 1, 1, 1),
            ("x^y", Qt.Key_G, self.on_clicked , 3, 2, 1, 1),
            ("7", Qt.Key_7, self.on_clicked , 3, 3, 1, 1),
            ("8", Qt.Key_8, self.on_clicked , 3, 4, 1, 1),
            ("9", Qt.Key_9, self.on_clicked , 3, 5, 1, 1),
            ("×", Qt.Key_multiply, self.on_clicked , 3, 6, 1, 1),
            ("Exit", Qt.Key_Exit, self.exit_clicked , 4, 0, 1, 1),
            ("(", Qt.Key_BracketRight, self.on_clicked , 4, 1, 1, 1),
            (")", Qt.Key_BracketLeft, self.on_clicked , 4, 2, 1, 1),
            ("C", Qt.Key_Clear, self.clear_clicked , 4, 3, 1, 1),
            ("0", Qt.Key_0, self.on_clicked , 4, 4, 1, 1),
            ("⌫", Qt.Key_Backspace, self.backspace_clicked , 4, 5, 1, 1),
            ("÷", Qt.Key_division, self.on_clicked , 4, 6, 1, 1),
        ]
        
        for text, key, func, y, x, height, width in keys:
            Button = QPushButton(self.KeypadWidget, text=text, focusPolicy=Qt.NoFocus)
            Button.setProperty("__key__", key)
            Button.setStyleSheet(DnI_buttons_style)
            
            sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(Button.sizePolicy().hasHeightForWidth())
            
            Button.setSizePolicy(sizePolicy)
            
            self.KeypadGridLayout.addWidget(Button, y, x, height, width)
            Button.clicked.connect(func)
            
        self.MainVerticalLayout.addWidget(self.KeypadWidget)

        
    def on_clicked(self):
        button = self.sender()
        if button.text() == "x^y":    
            text = "**"
        elif button.text() == "×":
            text = "*"
        elif button.text() == "÷":
            text = "/"
        else:    
            text = button.text()

        Key = button.property("__key__")
        Widget = QApplication.focusWidget()

        if hasattr(Key, "toPyObject"):
            Key = Key.toPyObject()
        if Widget:
            event = QKeyEvent(QEvent.KeyPress, Key, Qt.NoModifier, text)
            QCoreApplication.postEvent(Widget, event)
    def diff_clicked(self):
        data = self.InputLine.text()
        ans = str(sym.diff(data, x))
        self.OutputLine.setText(ans)
    def inte_clicked(self):
        data = self.InputLine.text()
        ans = str(sym.integrate(data, x))
        self.OutputLine.setText(ans)
    def clear_clicked(self):
        self.InputLine.setText("")
    def backspace_clicked(self):
        position = self.InputLine.cursorPosition()
        data = self.InputLine.text()
        data = data[:position-1] + data[position:]
        self.InputLine.setText(data)
    def exit_clicked(self):
        self.hide()
        self.ui_menu = Ui_Menu()
        self.ui_menu.show()
        
class Ui_Limits(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.resize(800, 800)
        self.InputWidget = QWidget(self)
        self.InputGridLayout = QGridLayout(self.InputWidget)
        
        self.FunctionLabel = QLabel("Function", self.InputWidget )
        self.AtpointLabel = QLabel("At Point", self.InputWidget )
        
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FunctionLabel.sizePolicy().hasHeightForWidth())
        self.FunctionLabel.setSizePolicy(sizePolicy)
        self.FunctionLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 87 24pt \"Arial Black\";")
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AtpointLabel.sizePolicy().hasHeightForWidth())
        self.AtpointLabel.setSizePolicy(sizePolicy)
        self.AtpointLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 87 24pt \"Arial Black\";")
        
        
        self.InputLine  = QLineEdit(self.InputWidget)
        self.AtpointLine = QLineEdit(self.InputWidget)
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputLine.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.AtpointLine.sizePolicy().hasHeightForWidth())
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        
        self.InputLine.setSizePolicy(sizePolicy)
        self.InputLine.setMinimumSize(QSize(0, 150))
        self.InputLine.setFont(font)
        self.InputLine.setStyleSheet("color: rgb(255, 255, 255);")
        self.InputLine.setText("")
        self.InputLine.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        self.AtpointLine.setSizePolicy(sizePolicy)
        self.AtpointLine.setMinimumSize(QSize(0, 150))
        self.AtpointLine.setFont(font)
        self.AtpointLine.setStyleSheet("color: rgb(255, 255, 255);")
        self.AtpointLine.setText("")
        self.AtpointLine.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        self.InputGridLayout.addWidget(self.InputLine, 0, 1)
        self.InputGridLayout.addWidget(self.AtpointLine, 1, 1)
        self.InputGridLayout.addWidget(self.FunctionLabel, 0, 0)
        self.InputGridLayout.addWidget(self.AtpointLabel, 1, 0)
        
        self.KeypadWidget = QWidget(self)
        self.KeypadGridLayout = QGridLayout(self.KeypadWidget)
        
        keys = [
            ("Limits", Qt.Key_L, self.lim_clicked , 0, 0, 1, 6),
            ("x", Qt.Key_X, self.on_clicked , 0, 6, 1, 1),
            ("sin()", Qt.Key_S, self.on_clicked , 1, 0, 1, 1),
            ("cos()", Qt.Key_C, self.on_clicked , 1, 1, 1, 1),
            ("tan()", Qt.Key_T, self.on_clicked , 1, 2, 1, 1),
            ("1", Qt.Key_1, self.on_clicked , 1, 3, 1, 1),
            ("2", Qt.Key_2, self.on_clicked , 1, 4, 1, 1),
            ("3", Qt.Key_3, self.on_clicked , 1, 5, 1, 1),
            ("+", Qt.Key_Plus, self.on_clicked , 1, 6, 1, 1),
            ("asin()", Qt.Key_L, self.on_clicked , 2, 0, 1, 1),
            ("acos()", Qt.Key_M, self.on_clicked , 2, 1, 1, 1),
            ("atan()", Qt.Key_N, self.on_clicked , 2, 2, 1, 1),
            ("4", Qt.Key_4, self.on_clicked , 2, 3, 1, 1),
            ("5", Qt.Key_5, self.on_clicked , 2, 4, 1, 1),
            ("6", Qt.Key_6, self.on_clicked , 2, 5, 1, 1),
            ("-", Qt.Key_Minus, self.on_clicked , 2, 6, 1, 1),
            ("e", Qt.Key_E, self.on_clicked , 3, 0, 1, 1),
            ("log()", Qt.Key_F, self.on_clicked , 3, 1, 1, 1),
            ("x^y", Qt.Key_G, self.on_clicked , 3, 2, 1, 1),
            ("7", Qt.Key_7, self.on_clicked , 3, 3, 1, 1),
            ("8", Qt.Key_8, self.on_clicked , 3, 4, 1, 1),
            ("9", Qt.Key_9, self.on_clicked , 3, 5, 1, 1),
            ("×", Qt.Key_multiply, self.on_clicked , 3, 6, 1, 1),
            ("Exit", Qt.Key_Exit, self.exit_clicked , 4, 0, 1, 1),
            ("(", Qt.Key_BracketRight, self.on_clicked , 4, 1, 1, 1),
            (")", Qt.Key_BracketLeft, self.on_clicked , 4, 2, 1, 1),
            ("C", Qt.Key_Clear, self.clear_clicked , 4, 3, 1, 1),
            ("0", Qt.Key_0, self.on_clicked , 4, 4, 1, 1),
            ("⌫", Qt.Key_Backspace, self.backspace_clicked , 4, 5, 1, 1),
            ("÷", Qt.Key_division, self.on_clicked , 4, 6, 1, 1),
        ]
        
        for text, key, func, y, x, height, width in keys:
            Button = QPushButton(self.KeypadWidget, text=text, focusPolicy=Qt.NoFocus)
            Button.setProperty("__key__", key)
            Button.setStyleSheet(Limits_buttons_style)
            
            sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(Button.sizePolicy().hasHeightForWidth())
            
            Button.setSizePolicy(sizePolicy)
            
            self.KeypadGridLayout.addWidget(Button, y, x, height, width)
            Button.clicked.connect(func)
            
        
        
        self.MainVerticalLayout = QVBoxLayout(self)
        self.MainVerticalLayout.addWidget(self.InputWidget)
        self.MainVerticalLayout.addWidget(self.KeypadWidget)
    def on_clicked(self):
        button = self.sender()
        if button.text() == "x^y":    
            text = "**"
        elif button.text() == "×":
            text = "*"
        elif button.text() == "÷":
            text = "/"
        else:    
            text = button.text()

        Key = button.property("__key__")
        Widget = QApplication.focusWidget()

        if hasattr(Key, "toPyObject"):
            Key = Key.toPyObject()
        if Widget:
            event = QKeyEvent(QEvent.KeyPress, Key, Qt.NoModifier, text)
            QCoreApplication.postEvent(Widget, event)
            
    def lim_clicked(self):
        data = self.InputLine.text()
        data_2 = self.AtpointLine.text()
        ans=str(sym.limit(data, x, data_2))
        ans = ("Answer: ") + ans
        self.InputLine.setText(ans)
        
    def clear_clicked(self):
        self.InputLine.setText("")
        self.AtpointLine.setText("")
        
    def backspace_clicked(self):
        position = self.InputLine.cursorPosition()
        data = self.InputLine.text()
        data = data[:position-1] + data[position:]
        self.InputLine.setText(data)
        
    def exit_clicked(self):
        self.hide()
        self.ui_menu = Ui_Menu()
        self.ui_menu.show()

class Ui_Roots(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.resize(800, 800)
        self.InputLine = QLineEdit(self)
        self.OutputLine = QLineEdit(self)
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputLine.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.OutputLine.sizePolicy().hasHeightForWidth())
        
        font = QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(True)
        
        
        self.InputLine.setSizePolicy(sizePolicy)
        self.InputLine.setFont(font)
        self.InputLine.setStyleSheet("color: rgb(255, 255, 255);")
        self.InputLine.setText("")
        self.InputLine.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        self.OutputLine.setSizePolicy(sizePolicy)
        self.OutputLine.setFont(font)
        self.OutputLine.setStyleSheet("color: rgb(255, 255, 255);")
        self.OutputLine.setText("")
        self.OutputLine.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Space = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.Space_2 = QSpacerItem(0, 100, QSizePolicy.Minimum, QSizePolicy.Maximum)
        
        self.SolveButton = QPushButton(self, text = "Solve")
        self.ExitButton = QPushButton(self, text="Exit")
        
        self.SolveButton.clicked.connect(self.solve_clicked)
        self.ExitButton.clicked.connect(self.exit_clicked)
        
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SolveButton.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.ExitButton.sizePolicy().hasHeightForWidth())
        self.SolveButton.setSizePolicy(sizePolicy)
        self.SolveButton.setStyleSheet(Roots_buttons_style)
        self.ExitButton.setSizePolicy(sizePolicy)
        self.ExitButton.setStyleSheet(Roots_buttons_style)
        
        
        self.MainVerticalLayout = QVBoxLayout(self)
        self.MainVerticalLayout.addItem(self.Space)
        self.MainVerticalLayout.addWidget(self.InputLine)
        self.MainVerticalLayout.addWidget(self.OutputLine)
        self.MainVerticalLayout.addItem(self.Space_2)
        self.MainVerticalLayout.addWidget(self.SolveButton)
        self.MainVerticalLayout.addWidget(self.ExitButton)
    
    def exit_clicked(self):
        self.hide()
        self.ui_menu = Ui_Menu()
        self.ui_menu.show()
    
    def solve_clicked(self):
        data = self.InputLine.text()
        answer= str(sym.solveset(data,x))
        self.OutputLine.setText(answer)    

class Ui_History(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 800)
        self.TableWidget = QWidget(self)
        self.TableWidget.setStyleSheet("QWidget {\n"
                        "    \n"
                        "    color: rgb(255, 255, 255);\n"
                        "    background-color: rgb(0, 0, 0);\n"
                        "    font: 87 16pt \"Arial Black\";\n"
                        "}\n"
                        "\n"
                        "QHeaderView::section:all\n"
                        "{\n"
                        "    font: 87 16pt \"Arial Black\";\n"
                        "    background-color: rgb(0, 0, 0);\n"
                        "    color: rgb(255, 255, 255);\n"
                        "}")
                
        self.TableVerticalLayout = QVBoxLayout(self.TableWidget)
        self.Table = QTableWidget(self.TableWidget)
        self.TableVerticalLayout.addWidget(self.Table)
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table.sizePolicy().hasHeightForWidth())
        self.Table.setSizePolicy(sizePolicy)
        self.Table.setMinimumSize(QSize(0, 0))
        self.Table.setAutoFillBackground(True)
        self.Table.setStyleSheet("QWidget {\n"
            "    \n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: rgb(0, 0, 0);\n"
            "    font: 87 16pt \"Arial Black\";\n"
            "}\n"
            "\n"
            "QHeaderView::section:all\n"
            "{\n"
            "    font: 87 16pt \"Arial Black\";\n"
            "    background-color: rgb(0, 0, 0);\n"
            "    color: rgb(255, 255, 255);\n"
            "}")
        self.Table.setLineWidth(1)
        self.Table.setMidLineWidth(0)
        self.Table.setRowCount(0)
        self.Table.setColumnCount(3)
        
        self.Table.setHorizontalHeaderLabels(['Type', 'Function', 'Answer'])
        
        self.header = self.Table.horizontalHeader()       
        self.header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        
        
        
        
        
        
        
        
        self.ButtonWidget = QWidget(self)
        self.ButtonHorizontalLayout = QHBoxLayout(self.ButtonWidget)
        keys = [("Clear", self.clear_clicked),
                ("Exit", self.exit_clicked)]
        for text, func in keys:
            self.button = QPushButton(self.ButtonWidget, text=text)
            self.ButtonHorizontalLayout.addWidget(self.button)
            self.button.clicked.connect(func)
            sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
            self.button.setSizePolicy(sizePolicy)
            self.button.setMinimumSize(QSize(0, 100))
            self.button.setStyleSheet(History_buttons_style)
    
        
        self.MainVerticalLayout = QVBoxLayout(self)
        self.MainVerticalLayout.addWidget(self.TableWidget)
        self.MainVerticalLayout.addWidget(self.ButtonWidget)
    def clear_clicked(self):
        pass
    
    def exit_clicked(self):
        self.hide()
        self.ui_menu = Ui_Menu()
        self.ui_menu.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ui_Menu()
    w.show()
    app.exec()