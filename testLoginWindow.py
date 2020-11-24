import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from testLogin import Ui_ventanaLogin
from ventana_crear_cuenta import Ui_ventana_crear_cuenta
from ventana_SGC import Ui_ventana_SGC


class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.ui = Ui_ventanaLogin()
        self.ui.setupUi(self)
        # your code ends here
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    #w.show()
    sys.exit(app.exec_())