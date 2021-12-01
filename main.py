

from app_window1 import *
from app_window2 import *
from app_window3 import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys
from datetime import datetime

authorization_time = ''

class Parent(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.button_check.clicked.connect(self.actionButtonCheck)

    def actionButtonCheck(self):
        global authorization_time
        authorization_time = str(current_datatime.hour) + ':' + str(current_datatime.minute)+ ':' + str(current_datatime.second)
        child.show()
        self.close()

class Child(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child_ui = Ui_Dialog()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.actionButton)

    def actionButton(self):
        print(authorization_time)
        child_2.show()
        self.close()

class Child_2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child_2_ui = Ui_Dialog1()
        self.child_2_ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Parent()
    child = Child()
    child_2 = Child_2()
    window.show()

    current_datatime = datetime.now()

    sys.exit(app.exec_())