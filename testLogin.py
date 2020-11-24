# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testLogin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventanaLogin(object):
    def setupUi(self, ventanaLogin):
        ventanaLogin.setObjectName("ventanaLogin")
        ventanaLogin.resize(400, 380)
        ventanaLogin.setMinimumSize(QtCore.QSize(400, 380))
        ventanaLogin.setMaximumSize(QtCore.QSize(400, 380))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/error_404-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ventanaLogin.setWindowIcon(icon)
        ventanaLogin.setStyleSheet("QWidget{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0.946, y2:0.159, stop:0 rgba(37, 1, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"\n"
"}\n"
"\n"
"QFrame#frame_bot{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0.445545, y2:0.863636, stop:0 rgba(11, 0, 37, 255), stop:1 rgba(0, 5, 64, 255));\n"
"}\n"
"\n"
"QFrame{\n"
"    \n"
"    background-image: url(:/images/images/darkBlueBackground.png);\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel{\n"
"    background: transparent;\n"
"    color: rgb(99, 245, 77);\n"
"    font-size: 20px;\n"
"    font: Ubuntu bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: white\n"
"}\n"
"\n"
"QPushButton{\n"
"color: white;\n"
"background: qlineargradient(spread:pad, x1:0.800995, y1:0.256182, x2:1, y2:0, stop:0 rgba(164, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QLabel#label_titulo{\n"
"    color: rgb(130, 251, 207);\n"
"    background: transparent;\n"
"    font-size: 24px;\n"
"    font-family: Sans;\n"
"}")
        self.label_usuario = QtWidgets.QLabel(ventanaLogin)
        self.label_usuario.setGeometry(QtCore.QRect(20, 190, 331, 28))
        self.label_usuario.setObjectName("label_usuario")
        self.frame_top = QtWidgets.QFrame(ventanaLogin)
        self.frame_top.setGeometry(QtCore.QRect(10, 10, 371, 91))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.label_error404 = QtWidgets.QLabel(self.frame_top)
        self.label_error404.setGeometry(QtCore.QRect(230, -10, 141, 111))
        self.label_error404.setText("")
        self.label_error404.setPixmap(QtGui.QPixmap(":/images/images/error404.png"))
        self.label_error404.setScaledContents(True)
        self.label_error404.setObjectName("label_error404")
        self.label_titulo = QtWidgets.QLabel(self.frame_top)
        self.label_titulo.setGeometry(QtCore.QRect(10, -10, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_titulo.setFont(font)
        self.label_titulo.setObjectName("label_titulo")
        self.comboBox = QtWidgets.QComboBox(ventanaLogin)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(20, 140, 280, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_cuenta = QtWidgets.QLabel(ventanaLogin)
        self.label_cuenta.setGeometry(QtCore.QRect(20, 120, 71, 17))
        self.label_cuenta.setObjectName("label_cuenta")
        self.lineEdit_user = QtWidgets.QLineEdit(ventanaLogin)
        self.lineEdit_user.setGeometry(QtCore.QRect(20, 220, 271, 26))
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(ventanaLogin)
        self.lineEdit_password.setGeometry(QtCore.QRect(20, 280, 271, 26))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_password = QtWidgets.QLabel(ventanaLogin)
        self.label_password.setGeometry(QtCore.QRect(20, 260, 131, 17))
        self.label_password.setObjectName("label_password")
        self.pushButton_login = QtWidgets.QPushButton(ventanaLogin)
        self.pushButton_login.setGeometry(QtCore.QRect(40, 330, 89, 25))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_register = QtWidgets.QPushButton(ventanaLogin)
        self.pushButton_register.setGeometry(QtCore.QRect(150, 330, 101, 25))
        self.pushButton_register.setObjectName("pushButton_register")
        self.pushButton_salir = QtWidgets.QPushButton(ventanaLogin)
        self.pushButton_salir.setGeometry(QtCore.QRect(270, 330, 89, 25))
        self.pushButton_salir.setObjectName("pushButton_salir")
        self.frame_bot = QtWidgets.QFrame(ventanaLogin)
        self.frame_bot.setGeometry(QtCore.QRect(10, 110, 371, 251))
        self.frame_bot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bot.setObjectName("frame_bot")
        self.frame_bot.raise_()
        self.frame_top.raise_()
        self.label_usuario.raise_()
        self.comboBox.raise_()
        self.label_cuenta.raise_()
        self.lineEdit_user.raise_()
        self.lineEdit_password.raise_()
        self.label_password.raise_()
        self.pushButton_login.raise_()
        self.pushButton_register.raise_()
        self.pushButton_salir.raise_()

        self.retranslateUi(ventanaLogin)
        QtCore.QMetaObject.connectSlotsByName(ventanaLogin)

    def retranslateUi(self, ventanaLogin):
        _translate = QtCore.QCoreApplication.translate
        ventanaLogin.setWindowTitle(_translate("ventanaLogin", "Iniciar sesión o registrarse"))
        self.label_usuario.setText(_translate("ventanaLogin", "Usuario"))
        self.label_titulo.setText(_translate("ventanaLogin", "Sistema de Gestión \n"
"Contable"))
        self.comboBox.setItemText(0, _translate("ventanaLogin", "Estandar"))
        self.comboBox.setItemText(1, _translate("ventanaLogin", "Administrador"))
        self.label_cuenta.setText(_translate("ventanaLogin", "Cuenta"))
        self.label_password.setText(_translate("ventanaLogin", "Contraseña"))
        self.pushButton_login.setText(_translate("ventanaLogin", "Ingresar"))
        self.pushButton_register.setText(_translate("ventanaLogin", "Crear cuenta"))
        self.pushButton_salir.setText(_translate("ventanaLogin", "Salir"))

import source

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaLogin = QtWidgets.QWidget()
    ui = Ui_ventanaLogin()
    ui.setupUi(ventanaLogin)
    ventanaLogin.show()
    sys.exit(app.exec_())

