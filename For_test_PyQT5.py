#Приложение с одним окном, написанное с помощью PyQt5 without Qt Designer
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
#QApplication - создаем приложение, в которому будут окна - QMainWindow
import sys #встроенная библиотека "system"

class First_Window(QMainWindow):
    def __init__(self):
        super(First_Window, self).__init__() #в конструкторе Python2 была необходимость писать super(First_Window, self).__init__()
                               #в Python3 эти 2 параметра осуществлены по умолчанию
        self.setWindowTitle("Тестовая программа")
        self.setGeometry(300, 250, 350, 200)

        self.text = QtWidgets.QLabel(self)
        self.text.setText("Это базовая надпись")
        self.text.move(100, 100)
        self.text.adjustSize() #размер виджета самостоятельно подгоняеться под размер надписи

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Нажми на кнопку")
        self.button.move(70, 150)
        self.button.setFixedWidth(200)



# def procedure():
#     window = QMainWindow()
#     window.setWindowTitle("Тестовая программа")
#     window.setGeometry(300, 250, 350, 200)
#
#     text = QtWidgets.QLabel(window)
#     text.setText("Это базовая надпись")
#     text.move(100, 100)
#     text.adjustSize()
#
#     button = QtWidgets.QPushButton(window)
#     button.setText("Нажми на кнопку")
#     button.move(70, 150)
#     button.setFixedWidth(200)
#
#     window.show()

def start_programm_for_procedure():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("Тестовая программа")
    window.setGeometry(300, 250, 350, 200)

    text = QtWidgets.QLabel(window)
    text.setText("Это базовая надпись")
    text.move(100, 100)
    text.adjustSize()

    button = QtWidgets.QPushButton(window)
    button.setText("Нажми на кнопку")
    button.move(70, 150)
    button.setFixedWidth(200)

    window.show()

    sys.exit(app.exec_())


def start_programm_for_FirstWindow():
    app = QApplication(sys.argv)
    x = First_Window()
    x.show()
    sys.exit(app.exec_())

start_programm_for_procedure()

#pyuic5 -x sign_in_2.ui -o sign_in_2.py