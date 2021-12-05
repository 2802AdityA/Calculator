from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QEvent, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QFont, QKeyEvent)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import sympy as sym
import sys

x = sym.Symbol('x')

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
menu_window_style = """background-image: url("wallpaper.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;"""
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

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)



class Ui_Menu(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.resize(800, 600)
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setStyleSheet(menu_window_style)
        self.VerticalLayout = QVBoxLayout(self.MainWidget)
        
        keys = [
            ("Differentiation and Integration", Qt.Key_A, self.common),
            ("Limits", Qt.Key_B, self.common),
            ("Roots", Qt.Key_C, self.common),
            ("History", Qt.Key_D, self.common),
        ]
        
        for text, key, func in keys:
            Button = QPushButton(self.MainWidget, text=text, focusPolicy=Qt.NoFocus)
            Button.setProperty("__key__", key)
            Button.setStyleSheet(menu_button_style)
            
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(Button.sizePolicy().hasHeightForWidth())
            Button.setSizePolicy(sizePolicy)
            
            Button.clicked.connect(func)
            self.VerticalLayout.addWidget(Button)
            


        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi
    
    def common(self):
        main_ui.close()
        
        
        
        # app = QtWidgets.QApplication(sys.argv)
        # main_window = QtWidgets.QMainWindow()
        
        dni_ui.show()
        
        
        
        

class Ui_DnI(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.resize(800, 600)
        
    
        self.Mainwidget = QWidget(MainWindow)
        self.Mainwidget.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.VerticalLayout = QVBoxLayout(self.Mainwidget)
        
        self.Inputwidget = QWidget(self.Mainwidget)
        self.VerticalLayout_2 = QVBoxLayout(self.Inputwidget)
        
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        
        self.InputlineEdit = QLineEdit(self.Inputwidget)
        self.OutputlineEdit = QLineEdit(self.Inputwidget)

        self.InputlineEdit.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        sizePolicy.setHeightForWidth(self.InputlineEdit.sizePolicy().hasHeightForWidth())
        self.InputlineEdit.setSizePolicy(sizePolicy)
        self.InputlineEdit.setMinimumSize(QSize(0, 150))
        self.InputlineEdit.setFont(font)
        self.InputlineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.InputlineEdit.setText("")
        
        self.OutputlineEdit.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        sizePolicy.setHeightForWidth(self.OutputlineEdit.sizePolicy().hasHeightForWidth())
        self.OutputlineEdit.setSizePolicy(sizePolicy)
        self.OutputlineEdit.setMinimumSize(QSize(0, 150))
        self.OutputlineEdit.setFont(font)
        self.OutputlineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.OutputlineEdit.setText("")
        
        self.VerticalLayout_2.addWidget(self.InputlineEdit)
        self.VerticalLayout_2.addWidget(self.OutputlineEdit)

        self.VerticalLayout.addWidget(self.Inputwidget)
        self.Keypadwidget = QWidget(self.Mainwidget)
        
        self.GridLayout = QGridLayout(self.Keypadwidget)
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
            Button = QPushButton(self.Keypadwidget, text=text, focusPolicy=Qt.NoFocus)
            Button.setProperty("__key__", key)
            Button.setStyleSheet(DnI_buttons_style)
            
            sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(Button.sizePolicy().hasHeightForWidth())
            
            Button.setSizePolicy(sizePolicy)
            
            self.GridLayout.addWidget(Button, y, x, height, width)
            Button.clicked.connect(func)
            
        self.VerticalLayout.addWidget(self.Keypadwidget)

        MainWindow.setCentralWidget(self.Mainwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi
    
    def on_clicked(self):
        button = self.sender()
        if button.text() == "x^y":    
            text = "**"
        elif button.text() == "×":
            text = "*"
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
        data = self.InputlineEdit.text()
        ans = str(sym.diff(data, x))
        self.OutputlineEdit.setText(ans)
    def inte_clicked(self):
        data = self.InputlineEdit.text()
        ans = str(sym.integrate(data, x))
        self.OutputlineEdit.setText(ans)
        
    def clear_clicked(self):
        self.InputlineEdit.setText("")
    
    def backspace_clicked(self):
        position = self.InputlineEdit.cursorPosition()
        data = self.InputlineEdit.text()
        data = data[:position-1] + data[position:]
        self.InputlineEdit.setText(data)
        
    def exit_clicked(self):
        # ui.show()
        main_ui.hide()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    
    
    main_ui = MainWindow()
    
    dni_ui = Ui_DnI()
    dni_ui.setupUi(main_window)
    
    main_ui.show()
    app.exec()
    del app