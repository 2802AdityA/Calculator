from PySide6.QtCore import (QCoreApplication, QEvent, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QKeyEvent)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import sympy as sym
x = sym.Symbol('x')
style = ("QPushButton{\n"
         "   font: 87 20pt \"Arial Black\";\n"
         "   color: rgb(255, 255, 255);\n"
         "   background-color: rgb(0, 0, 0);\n"
         "   border-radius: 35-px;\n"
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

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
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
            ("Differentiate", Qt.Key_D, 0, 0, 1, 3),
            ("Integrate", Qt.Key_I, 0, 3, 1, 3),
            ("x", Qt.Key_X, 0, 6, 1, 1),
            ("sin()", Qt.Key_S, 1, 0, 1, 1),
            ("cos()", Qt.Key_C, 1, 1, 1, 1),
            ("tan()", Qt.Key_T, 1, 2, 1, 1),
            ("1", Qt.Key_1, 1, 3, 1, 1),
            ("2", Qt.Key_2, 1, 4, 1, 1),
            ("3", Qt.Key_3, 1, 5, 1, 1),
            ("+", Qt.Key_Plus, 1, 6, 1, 1),
            ("asin()", Qt.Key_L, 2, 0, 1, 1),
            ("acos()", Qt.Key_M, 2, 1, 1, 1),
            ("atan()", Qt.Key_N, 2, 2, 1, 1),
            ("4", Qt.Key_4, 2, 3, 1, 1),
            ("5", Qt.Key_5, 2, 4, 1, 1),
            ("6", Qt.Key_6, 2, 5, 1, 1),
            ("-", Qt.Key_Minus, 2, 6, 1, 1),
            ("e", Qt.Key_E, 3, 0, 1, 1),
            ("log()", Qt.Key_F, 3, 1, 1, 1),
            ("x^y", Qt.Key_G, 3, 2, 1, 1),
            ("7", Qt.Key_7, 3, 3, 1, 1),
            ("8", Qt.Key_8, 3, 4, 1, 1),
            ("9", Qt.Key_9, 3, 5, 1, 1),
            ("×", Qt.Key_multiply, 3, 6, 1, 1),
            ("Exit", Qt.Key_Exit, 4, 0, 1, 1),
            ("(", Qt.Key_BracketRight, 4, 1, 1, 1),
            (")", Qt.Key_BracketLeft, 4, 2, 1, 1),
            ("C", Qt.Key_Clear, 4, 3, 1, 1),
            ("0", Qt.Key_0, 4, 4, 1, 1),
            ("⌫", Qt.Key_Backspace, 4, 5, 1, 1),
            ("÷", Qt.Key_division, 4, 6, 1, 1),
        ]
        
        for text, key, y, x, height, width in keys:
            
            TEXT = ["x", "sin()", "cos()", "tan()", "1", "2", "3", "+", "asin()", "acos()",
                    "atan()", "x^y", "4", "5", "6", "-", "e", "log()", "7", "8", "9", "×", "(", ")", "0", "÷", "×"]
            
            Button = QPushButton(self.Keypadwidget, text=text, focusPolicy=Qt.NoFocus)
            Button.setProperty("__key__", key)
            Button.setStyleSheet(style)
            
            sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(Button.sizePolicy().hasHeightForWidth())
            
            Button.setSizePolicy(sizePolicy)
            
            self.GridLayout.addWidget(Button, y, x, height, width)
            if text in TEXT:
                Button.clicked.connect(self.on_clicked)
            elif text=="Differentiate":
                Button.clicked.connect(self.diff_clicked)
            elif text=="Integrate":
                Button.clicked.connect(self.inte_clicked)
            elif text=="C":
                Button.clicked.connect(self.clear)

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
        
    def clear(self):
        self.InputlineEdit.setText("")
    
    def backspace(self):
        data = self.InputlineEdit.text()
        data = data[:-1]
        self.InputlineEdit.setText(data)