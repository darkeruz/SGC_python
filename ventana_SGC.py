# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_SGC.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventana_SGC(object):
    def setupUi(self, ventana_SGC):
        ventana_SGC.setObjectName("ventana_SGC")
        ventana_SGC.resize(480, 497)
        ventana_SGC.setMinimumSize(QtCore.QSize(480, 497))
        ventana_SGC.setMaximumSize(QtCore.QSize(480, 497))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/error_404-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ventana_SGC.setWindowIcon(icon)
        ventana_SGC.setStyleSheet("QWidget{\n"
"        background: qlineargradient(spread:pad, x1:0, y1:1, x2:0.946, y2:0.159, stop:0 rgba(37, 1, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"}\n"
"\n"
"QFrame#frame_top{\n"
"background-image: url(:/images/images/darkBlueBackground.png);\n"
"\n"
"    border-radius: 15px;\n"
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
"QLabel#label_404{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QLabel#label_titulo{\n"
"    color: rgb(130, 251, 207);\n"
"    background: transparent;\n"
"    font-size: 28px;\n"
"    font-family: Sans;\n"
"}\n"
"\n"
"QPushButton#pushButton_salir{\n"
"color: white;\n"
"background: qlineargradient(spread:pad, x1:0.800995, y1:0.256182, x2:1, y2:0, stop:0 rgba(164, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QPushButton#pushButton_registrarMovimientos{\n"
"    background: qlineargradient(spread:pad, x1:0.93, y1:0.147727, x2:1, y2:0, stop:0 rgba(0, 19, 144, 243), stop:1 rgba(255, 255, 255, 255));\n"
"    color: white;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton#pushButton_realizarConsultas{\n"
"    background: qlineargradient(spread:pad, x1:0.93, y1:0.147727, x2:1, y2:0, stop:0 rgba(0, 19, 144, 243), stop:1 rgba(255, 255, 255, 255));\n"
"    color: white;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QLabel#label_realizarConsultas{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QLabel#label_registrarMovimientos{\n"
"    background: transparent;\n"
"}")
        self.frame_top = QtWidgets.QFrame(ventana_SGC)
        self.frame_top.setGeometry(QtCore.QRect(10, 20, 461, 111))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.label_404 = QtWidgets.QLabel(self.frame_top)
        self.label_404.setGeometry(QtCore.QRect(260, -10, 211, 141))
        self.label_404.setText("")
        self.label_404.setPixmap(QtGui.QPixmap(":/images/images/error404.png"))
        self.label_404.setScaledContents(True)
        self.label_404.setObjectName("label_404")
        self.label_titulo = QtWidgets.QLabel(self.frame_top)
        self.label_titulo.setGeometry(QtCore.QRect(10, 30, 291, 61))
        self.label_titulo.setObjectName("label_titulo")
        self.frame_bottom = QtWidgets.QFrame(ventana_SGC)
        self.frame_bottom.setGeometry(QtCore.QRect(10, 170, 461, 311))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.pushButton_salir = QtWidgets.QPushButton(self.frame_bottom)
        self.pushButton_salir.setGeometry(QtCore.QRect(360, 260, 89, 25))
        self.pushButton_salir.setObjectName("pushButton_salir")
        self.pushButton_registrarMovimientos = QtWidgets.QPushButton(self.frame_bottom)
        self.pushButton_registrarMovimientos.setGeometry(QtCore.QRect(11, 130, 151, 81))
        self.pushButton_registrarMovimientos.setObjectName("pushButton_registrarMovimientos")
        self.pushButton_realizarConsultas = QtWidgets.QPushButton(self.frame_bottom)
        self.pushButton_realizarConsultas.setGeometry(QtCore.QRect(11, 20, 151, 81))
        self.pushButton_realizarConsultas.setObjectName("pushButton_realizarConsultas")
        self.label_realizarConsultas = QtWidgets.QLabel(self.frame_bottom)
        self.label_realizarConsultas.setGeometry(QtCore.QRect(300, 20, 101, 81))
        self.label_realizarConsultas.setText("")
        self.label_realizarConsultas.setPixmap(QtGui.QPixmap(":/images/images/consultar.png"))
        self.label_realizarConsultas.setScaledContents(True)
        self.label_realizarConsultas.setObjectName("label_realizarConsultas")
        self.label_registrarMovimientos = QtWidgets.QLabel(self.frame_bottom)
        self.label_registrarMovimientos.setGeometry(QtCore.QRect(280, 120, 141, 101))
        self.label_registrarMovimientos.setText("")
        self.label_registrarMovimientos.setPixmap(QtGui.QPixmap(":/images/images/RegistrarMovimientos.png"))
        self.label_registrarMovimientos.setScaledContents(True)
        self.label_registrarMovimientos.setObjectName("label_registrarMovimientos")

        self.retranslateUi(ventana_SGC)
        QtCore.QMetaObject.connectSlotsByName(ventana_SGC)

    def retranslateUi(self, ventana_SGC):
        _translate = QtCore.QCoreApplication.translate
        ventana_SGC.setWindowTitle(_translate("ventana_SGC", "Sistema de Gestión Contable"))
        self.label_titulo.setText(_translate("ventana_SGC", "Sistema de Gestión \n"
"Contable"))
        self.pushButton_salir.setText(_translate("ventana_SGC", "Salir"))
        self.pushButton_registrarMovimientos.setText(_translate("ventana_SGC", "Registrar \n"
"movimientos"))
        self.pushButton_realizarConsultas.setText(_translate("ventana_SGC", "Realizar \n"
"consultas"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_SGC = QtWidgets.QWidget()
    ui = Ui_ventana_SGC()
    ui.setupUi(ventana_SGC)
    ventana_SGC.show()
    sys.exit(app.exec_())

