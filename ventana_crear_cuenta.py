# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_crear_cuenta.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana_crear_cuenta(object):
    def setupUi(self, ventana_crear_cuenta):
        ventana_crear_cuenta.setObjectName("ventana_crear_cuenta")
        ventana_crear_cuenta.resize(640, 480)
        ventana_crear_cuenta.setMinimumSize(QtCore.QSize(640, 480))
        ventana_crear_cuenta.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/error_404-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ventana_crear_cuenta.setWindowIcon(icon)
        ventana_crear_cuenta.setStyleSheet("QWidget{\n"
"background-color: rgb(52, 2, 2);\n"
"\n"
"}\n"
"\n"
"QFrame#frame_bottom{\n"
"    width: 260px;\n"
"    height: 260px;\n"
"    border-radius: 15px;\n"
"    \n"
"    background-image: url(:/images/images/fondoRojo.jpeg);\n"
"\n"
"}\n"
"\n"
"QFrame#frame_top{\n"
"    background-image: url(:/images/images/fondoRojo.jpeg);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel#label_titulo{\n"
"    color: white;\n"
"    background: transparent;\n"
"    font-size: 33px;\n"
"    font-family: Arial Black;\n"
"}\n"
"\n"
"QLabel#label_error404{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QLabel{\n"
"    background: transparent;\n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font: Ubuntu bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: black;\n"
"    background: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: white;\n"
"background: qlineargradient(spread:pad, x1:0.800995, y1:0.256182, x2:1, y2:0, stop:0 rgba(164, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.frame_bottom = QtWidgets.QFrame(ventana_crear_cuenta)
        self.frame_bottom.setGeometry(QtCore.QRect(10, 110, 621, 361))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.label_correo = QtWidgets.QLabel(self.frame_bottom)
        self.label_correo.setGeometry(QtCore.QRect(11, 150, 68, 24))
        self.label_correo.setObjectName("label_correo")
        self.label_apellido = QtWidgets.QLabel(self.frame_bottom)
        self.label_apellido.setGeometry(QtCore.QRect(11, 57, 80, 24))
        self.label_apellido.setObjectName("label_apellido")
        self.lineEdit_apellido = QtWidgets.QLineEdit(self.frame_bottom)
        self.lineEdit_apellido.setGeometry(QtCore.QRect(209, 26, 371, 25))
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.label_nombre_usuario = QtWidgets.QLabel(self.frame_bottom)
        self.label_nombre_usuario.setGeometry(QtCore.QRect(11, 88, 192, 24))
        self.label_nombre_usuario.setObjectName("label_nombre_usuario")
        self.label_password = QtWidgets.QLabel(self.frame_bottom)
        self.label_password.setGeometry(QtCore.QRect(11, 119, 115, 24))
        self.label_password.setObjectName("label_password")
        self.lineEdit_nombre = QtWidgets.QLineEdit(self.frame_bottom)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(209, 57, 371, 25))
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.lineEdit_nombre_usuario = QtWidgets.QLineEdit(self.frame_bottom)
        self.lineEdit_nombre_usuario.setGeometry(QtCore.QRect(209, 88, 371, 25))
        self.lineEdit_nombre_usuario.setObjectName("lineEdit_nombre_usuario")
        self.label_nombre = QtWidgets.QLabel(self.frame_bottom)
        self.label_nombre.setGeometry(QtCore.QRect(11, 26, 81, 24))
        self.label_nombre.setObjectName("label_nombre")
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame_bottom)
        self.lineEdit_password.setGeometry(QtCore.QRect(209, 119, 371, 25))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_correo = QtWidgets.QLineEdit(self.frame_bottom)
        self.lineEdit_correo.setGeometry(QtCore.QRect(209, 150, 371, 25))
        self.lineEdit_correo.setObjectName("lineEdit_correo")
        self.label_gobierno = QtWidgets.QLabel(self.frame_bottom)
        self.label_gobierno.setGeometry(QtCore.QRect(0, 270, 641, 81))
        self.label_gobierno.setText("")
        self.label_gobierno.setPixmap(QtGui.QPixmap(":/images/images/parte_inferior1.jpg"))
        self.label_gobierno.setScaledContents(True)
        self.label_gobierno.setObjectName("label_gobierno")
        self.label_codigo_admin = QtWidgets.QLabel(self.frame_bottom)
        self.label_codigo_admin.setGeometry(QtCore.QRect(10, 180, 181, 24))
        self.label_codigo_admin.setObjectName("label_codigo_admin")
        self.lineEdit_codigo_admin = QtWidgets.QLineEdit(self.frame_bottom)
        self.lineEdit_codigo_admin.setGeometry(QtCore.QRect(210, 180, 371, 25))
        self.lineEdit_codigo_admin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_codigo_admin.setObjectName("lineEdit_codigo_admin")
        self.layoutWidget = QtWidgets.QWidget(self.frame_bottom)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 230, 621, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_register = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_register.setObjectName("pushButton_register")
        self.horizontalLayout.addWidget(self.pushButton_register)
        self.pushButton_salir = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_salir.setObjectName("pushButton_salir")
        self.horizontalLayout.addWidget(self.pushButton_salir)
        self.frame_top = QtWidgets.QFrame(ventana_crear_cuenta)
        self.frame_top.setGeometry(QtCore.QRect(10, 10, 621, 91))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.label_titulo = QtWidgets.QLabel(self.frame_top)
        self.label_titulo.setGeometry(QtCore.QRect(10, -20, 611, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.label_error404 = QtWidgets.QLabel(ventana_crear_cuenta)
        self.label_error404.setGeometry(QtCore.QRect(300, 70, 71, 71))
        self.label_error404.setText("")
        self.label_error404.setPixmap(QtGui.QPixmap(":/images/images/crearUsuario.png"))
        self.label_error404.setScaledContents(True)
        self.label_error404.setObjectName("label_error404")

        self.retranslateUi(ventana_crear_cuenta)
        QtCore.QMetaObject.connectSlotsByName(ventana_crear_cuenta)

    def retranslateUi(self, ventana_crear_cuenta):
        _translate = QtCore.QCoreApplication.translate
        ventana_crear_cuenta.setWindowTitle(_translate("ventana_crear_cuenta", "Crear Cuenta"))
        self.label_correo.setText(_translate("ventana_crear_cuenta", "Correo"))
        self.label_apellido.setText(_translate("ventana_crear_cuenta", "Nombre"))
        self.label_nombre_usuario.setText(_translate("ventana_crear_cuenta", "Nombre de usuario"))
        self.label_password.setText(_translate("ventana_crear_cuenta", "Contrase??a"))
        self.label_nombre.setText(_translate("ventana_crear_cuenta", "Apellido "))
        self.label_codigo_admin.setText(_translate("ventana_crear_cuenta", "C??digo de Admin"))
        self.pushButton_register.setText(_translate("ventana_crear_cuenta", "Crear"))
        self.pushButton_salir.setText(_translate("ventana_crear_cuenta", "Salir"))
        self.label_titulo.setText(_translate("ventana_crear_cuenta", "Sistema de Gesti??n Contable"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_crear_cuenta = QtWidgets.QWidget()
    ui = Ui_ventana_crear_cuenta()
    ui.setupUi(ventana_crear_cuenta)
    ventana_crear_cuenta.show()
    sys.exit(app.exec_())
