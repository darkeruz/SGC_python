# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_realizar_consulta.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana_realizar_consulta(object):
    def setupUi(self, ventana_realizar_consulta):
        ventana_realizar_consulta.setObjectName("ventana_realizar_consulta")
        ventana_realizar_consulta.resize(480, 640)
        ventana_realizar_consulta.setMinimumSize(QtCore.QSize(480, 640))
        ventana_realizar_consulta.setMaximumSize(QtCore.QSize(480, 640))
        ventana_realizar_consulta.setStyleSheet("QWidget{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0.946, y2:0.159, stop:0 rgba(37, 1, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"}\n"
"\n"
"QFrame#frame_top{    \n"
"    background-image: url(:/images/images/backgroundDarkRed.jpg);\n"
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
"QFrame#frame_bottom{\n"
"    width: 260px;\n"
"    height: 260px;\n"
"    border-radius: 15px;    \n"
"    border-image: url(:/images/images/backgroundDarkRed.jpg);\n"
"    display: none;\n"
"}\n"
"\n"
"QListWidget{    \n"
"    background-color: black;\n"
"    border-radius: 15px;\n"
"    color: rgb(99, 245, 77);\n"
"}\n"
"\n"
"QLabel#label_descripcion{\n"
"    background: transparent;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-family: Sans;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_top = QtWidgets.QFrame(ventana_realizar_consulta)
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
        self.label_error404.setGeometry(QtCore.QRect(300, 0, 161, 111))
        self.label_error404.setText("")
        self.label_error404.setPixmap(QtGui.QPixmap(":/images/images/error_404-2.png"))
        self.label_error404.setScaledContents(True)
        self.label_error404.setObjectName("label_error404")
        self.frame_bottom = QtWidgets.QFrame(ventana_realizar_consulta)
        self.frame_bottom.setGeometry(QtCore.QRect(20, 150, 441, 471))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.listWidget = QtWidgets.QListWidget(self.frame_bottom)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 421, 401))
        self.listWidget.setObjectName("listWidget")
        self.label_descripcion = QtWidgets.QLabel(self.frame_bottom)
        self.label_descripcion.setGeometry(QtCore.QRect(10, -10, 411, 71))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_descripcion.setFont(font)
        self.label_descripcion.setTextFormat(QtCore.Qt.PlainText)
        self.label_descripcion.setObjectName("label_descripcion")
        self.frame_bottom.raise_()
        self.frame_top.raise_()

        self.retranslateUi(ventana_realizar_consulta)
        QtCore.QMetaObject.connectSlotsByName(ventana_realizar_consulta)

    def retranslateUi(self, ventana_realizar_consulta):
        _translate = QtCore.QCoreApplication.translate
        ventana_realizar_consulta.setWindowTitle(_translate("ventana_realizar_consulta", "Realizar consultas"))
        self.label_titulo.setText(_translate("ventana_realizar_consulta", "Sistema de Gestión \n"
"Contable"))
        self.label_descripcion.setText(_translate("ventana_realizar_consulta", "Aquí se muestran todos los movimientos\n"
" registrados en el sistema"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_realizar_consulta = QtWidgets.QWidget()
    ui = Ui_ventana_realizar_consulta()
    ui.setupUi(ventana_realizar_consulta)
    ventana_realizar_consulta.show()
    sys.exit(app.exec_())
