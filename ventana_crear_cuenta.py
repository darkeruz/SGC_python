# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_crear_cuenta.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventana_crear_cuenta(object):
    def setupUi(self, ventana_crear_cuenta):
        ventana_crear_cuenta.setObjectName("ventana_crear_cuenta")
        ventana_crear_cuenta.resize(480, 457)
        ventana_crear_cuenta.setMinimumSize(QtCore.QSize(480, 457))
        ventana_crear_cuenta.setMaximumSize(QtCore.QSize(480, 457))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/error_404-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ventana_crear_cuenta.setWindowIcon(icon)
        ventana_crear_cuenta.setStyleSheet("QWidget{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0.946, y2:0.159, stop:0 rgba(37, 1, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"\n"
"/*rgb(46, 52, 54)*/\n"
"\n"
"}\n"
"\n"
"QFrame#frame_bottom{\n"
"    width: 260px;\n"
"    height: 260px;\n"
"    border-radius: 15px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0.445545, y2:0.863636, stop:0 rgba(11, 0, 37, 255), stop:1 rgba(0, 5, 64, 255));\n"
"    display: none;\n"
"}\n"
"\n"
"QFrame#frame_top{\n"
"    \n"
"    background-image: url(:/images/images/darkBlueBackground.png);\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel#label_titulo{\n"
"    color: rgb(130, 251, 207);\n"
"    background: transparent;\n"
"    font-size: 28px;\n"
"    font-family: Sans;\n"
"}\n"
"\n"
"QLabel#label_error404{\n"
"    background: transparent;\n"
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
"    color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: white;\n"
"background: qlineargradient(spread:pad, x1:0.800995, y1:0.256182, x2:1, y2:0, stop:0 rgba(164, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.frame_bottom = QtWidgets.QFrame(ventana_crear_cuenta)
        self.frame_bottom.setGeometry(QtCore.QRect(20, 150, 441, 291))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.pushButton_register = QtWidgets.QPushButton(self.frame_bottom)
        self.pushButton_register.setGeometry(QtCore.QRect(10, 210, 221, 41))
        self.pushButton_register.setObjectName("pushButton_register")
        self.pushButton_salir = QtWidgets.QPushButton(self.frame_bottom)
        self.pushButton_salir.setGeometry(QtCore.QRect(320, 210, 111, 41))
        self.pushButton_salir.setObjectName("pushButton_salir")
        self.label_correo = QtWidgets.QLabel(self.frame_bottom)
        self.label_correo.setGeometry(QtCore.QRect(11, 145, 68, 24))
        self.label_correo.setObjectName("label_correo")
        self.label_apellido = QtWidgets.QLabel(self.frame_bottom)
        self.label_apellido.setGeometry(QtCore.QRect(11, 52, 80, 24))
        self.label_apellido.setObjectName("label_apellido")
        self.lineEdit_apellido = QtWidgets.QLineEdit(self.frame_bottom)
        self.lineEdit_apellido.setGeometry(QtCore.QRect(209, 21, 221, 25))
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.label_nombre_usuario = QtWidgets.QLabel(self.frame_bottom)
        self.label_nombre_usuario.setGeometry(QtCore.QRect(11, 83, 192, 24))
        self.label_nombre_usuario.setObjectName("label_nombre_usuario")
        self.label_password = QtWidgets.QLabel(self.frame_bottom)
        self.label_password.setGeometry(QtCore.QRect(11, 114, 115, 24))
        self.label_password.setObjectName("label_password")
        self.lineEdit_nombre = QtWidgets.QLineEdit(self.frame_bottom)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(209, 52, 221, 25))
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.lineEdit_nombre_usuario = QtWidgets.QLineEdit(self.frame_bottom)
        self.lineEdit_nombre_usuario.setGeometry(QtCore.QRect(209, 83, 221, 25))
        self.lineEdit_nombre_usuario.setObjectName("lineEdit_nombre_usuario")
        self.label_nombre = QtWidgets.QLabel(self.frame_bottom)
        self.label_nombre.setGeometry(QtCore.QRect(11, 21, 81, 24))
        self.label_nombre.setObjectName("label_nombre")
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame_bottom)
        self.lineEdit_password.setGeometry(QtCore.QRect(209, 114, 221, 25))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_correo = QtWidgets.QLineEdit(self.frame_bottom)
        self.lineEdit_correo.setGeometry(QtCore.QRect(209, 145, 221, 25))
        self.lineEdit_correo.setObjectName("lineEdit_correo")
        self.frame_top = QtWidgets.QFrame(ventana_crear_cuenta)
        self.frame_top.setGeometry(QtCore.QRect(10, 20, 461, 111))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.label_titulo = QtWidgets.QLabel(self.frame_top)
        self.label_titulo.setGeometry(QtCore.QRect(10, 0, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_titulo.setFont(font)
        self.label_titulo.setObjectName("label_titulo")
        self.label_error404 = QtWidgets.QLabel(self.frame_top)
        self.label_error404.setGeometry(QtCore.QRect(250, 0, 211, 121))
        self.label_error404.setText("")
        self.label_error404.setPixmap(QtGui.QPixmap(":/images/images/error404.png"))
        self.label_error404.setScaledContents(True)
        self.label_error404.setObjectName("label_error404")

        self.retranslateUi(ventana_crear_cuenta)
        QtCore.QMetaObject.connectSlotsByName(ventana_crear_cuenta)

    def retranslateUi(self, ventana_crear_cuenta):
        _translate = QtCore.QCoreApplication.translate
        ventana_crear_cuenta.setWindowTitle(_translate("ventana_crear_cuenta", "Crear Cuenta"))
        self.pushButton_register.setText(_translate("ventana_crear_cuenta", "Crear"))
        self.pushButton_salir.setText(_translate("ventana_crear_cuenta", "Salir"))
        self.label_correo.setText(_translate("ventana_crear_cuenta", "Correo"))
        self.label_apellido.setText(_translate("ventana_crear_cuenta", "Nombre"))
        self.label_nombre_usuario.setText(_translate("ventana_crear_cuenta", "Nombre de usuario"))
        self.label_password.setText(_translate("ventana_crear_cuenta", "Contraseña"))
        self.label_nombre.setText(_translate("ventana_crear_cuenta", "Apellido "))
        self.label_titulo.setText(_translate("ventana_crear_cuenta", "Sistema de Gestión \n"
"Contable"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_crear_cuenta = QtWidgets.QWidget()
    ui = Ui_ventana_crear_cuenta()
    ui.setupUi(ventana_crear_cuenta)
    ventana_crear_cuenta.show()
    sys.exit(app.exec_())

