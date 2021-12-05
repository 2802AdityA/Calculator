from DI_UI import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
import sys
# from try_1 import Ui_MainWindowww
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        # self.ui_2 = Ui_MainWindowww()
        # self.ui_2.setupUi(self)
        self.ui.setupUi(self)
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())