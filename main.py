from PySide6.QtCore import (QCoreApplication, QEvent, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QKeyEvent)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit, QMainWindow,QPushButton, QSizePolicy, QVBoxLayout, QWidget)
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
            ("Roots", Qt.Key_C, self.show_new_window),
            ("History", Qt.Key_D, self.show_new_window),
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
    
    def show_new_window(self):
        pass
        
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
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ui_Menu()
    w.show()
    app.exec()