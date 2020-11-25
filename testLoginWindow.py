import sys
from PyQt5 import Qt
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from testLogin import Ui_ventanaLogin
from ventana_crear_cuenta import Ui_ventana_crear_cuenta
from ventana_SGC import Ui_ventana_SGC
import sqlite3

class ventanaCrearCuenta(qtw.QWidget, Ui_ventana_crear_cuenta):
    def __init__(self):
        super().__init__()

class ventanaSGC(qtw.QWidget, Ui_ventana_SGC):
    def __init__(self):
        super().__init__()

    def boton_salir_SGC(self):
        self.close()



class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        #self.ui_crear_cuenta2 = Ui_ventana_crear_cuenta()
        #self.ui_crear_cuenta2.setupUi(self)
        self.uiLogin = Ui_ventanaLogin()
        self.uiLogin.setupUi(self)
        self.setGeometry(qtc.QRect(800,250,0,0))


        #Si clickeamos en el boton de Salir, llamamos a la funcion boton_salir()
        self.uiLogin.pushButton_salir.clicked.connect(self.boton_salir)
        #Si usamos el metodo "setAutoDefault(True)" en un boton, este emitira la señal de "clicked" cuando presionemos enter
        self.uiLogin.pushButton_salir.setAutoDefault(True)
        self.uiLogin.pushButton_register.setAutoDefault(True)
        self.uiLogin.pushButton_login.setAutoDefault(True)
        #Si clickeamos el boton Login ingresamos a la funcion login_check()
        self.uiLogin.pushButton_login.clicked.connect(self.login_check)

        #Si clickeamos el boton de registrarse abrimos la ventana para la creacion de cuentas
        self.uiLogin.pushButton_register.clicked.connect(self.ventana_registrarse)

        # your code ends here
        self.show()

    def boton_salir(self):
        self.close()

    def login_check(self):
        conexion = sqlite3.connect('LoginBD.bd')
        cursor = conexion.cursor()

        username = self.uiLogin.lineEdit_user.text()
        password = self.uiLogin.lineEdit_password.text()

        try:
            result = cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario == '{}' AND password == '{}'".format(username, password)).fetchall()
            if(len(result) > 0):
                self.uiSGC = ventanaSGC()
                self.uiSGC.setupUi(self.uiSGC)
                self.uiSGC.setGeometry(qtc.QRect(800,250,0,0))
                self.uiSGC.pushButton_salir.setAutoDefault(True)
                self.uiSGC.pushButton_salir.clicked.connect(self.uiSGC.boton_salir_SGC)
                self.uiSGC.show()
                self.close()

            else:
                qtw.QMessageBox.critical(self, "Datos incorrectos", "El usuario o la contraseña ingresada no son correctos.")
        except sqlite3.OperationalError:
            qtw.QMessageBox.information(self, "Primero debes registrarte!", "Antes de iniciar sesión debes crear tu cuenta")

        conexion.close()

    def ventana_registrarse(self):
        self.uiVentanaCrearCuenta = ventanaCrearCuenta()
        self.uiVentanaCrearCuenta.setupUi(self.uiVentanaCrearCuenta)
        self.uiVentanaCrearCuenta.setGeometry(qtc.QRect(800,300,0,0))
        self.uiVentanaCrearCuenta.pushButton_salir.clicked.connect(self.boton_salir_ventana_crear_cuenta)
        self.uiVentanaCrearCuenta.show()
        self.uiVentanaCrearCuenta.pushButton_register.clicked.connect(self.boton_crear_cuenta)
        self.uiVentanaCrearCuenta.pushButton_register.setAutoDefault(True)
        self.uiVentanaCrearCuenta.pushButton_salir.setAutoDefault(True)

    def boton_salir_ventana_crear_cuenta(self):
        self.uiVentanaCrearCuenta.close()

    def boton_crear_cuenta(self):
        conexion = sqlite3.connect('LoginBD.bd')
        cursor = conexion.cursor()

        apellido = self.uiVentanaCrearCuenta.lineEdit_apellido.text()
        nombre = self.uiVentanaCrearCuenta.lineEdit_nombre.text()
        nombre_usuario = self.uiVentanaCrearCuenta.lineEdit_nombre_usuario.text()
        contraseña = self.uiVentanaCrearCuenta.lineEdit_password.text()
        correo = self.uiVentanaCrearCuenta.lineEdit_correo.text()

        if apellido == '' or nombre == '' or nombre_usuario == '' or contraseña == '' or correo == '':
            apellido = None
            nombre = None
            nombre_usuario = None
            contraseña = None
            correo = None

        user = [(apellido, nombre, nombre_usuario, contraseña, correo)]

        try:
            cursor.execute("""CREATE TABLE usuarios(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            apellido VARCHAR(50) UNIQUE NOT NULL,
                            nombre VARCHAR(50) NOT NULL,
                            nombre_usuario VARCHAR(50) NOT NULL,
                            password VARCHAR(50) NOT NULL,
                            correo VARCHAR(50) NOT NULL)""")

        except sqlite3.OperationalError:
            pass

        try:
            cursor.executemany("INSERT INTO usuarios VALUES (NULL, ?, ?, ?, ?, ?)", user).fetchall()
        except sqlite3.IntegrityError:
            qtw.QMessageBox.critical(self, "No se pudo registrar", "Asegurese de llenar correctamente todos los campos, si el problema persiste, es posible que el nombre de usuario elegido ya exista.")

        conexion.commit()
        conexion.close()
        self.uiVentanaCrearCuenta.lineEdit_apellido.setText("")
        self.uiVentanaCrearCuenta.lineEdit_nombre.setText("")
        self.uiVentanaCrearCuenta.lineEdit_nombre_usuario.setText("")
        self.uiVentanaCrearCuenta.lineEdit_password.setText("")
        self.uiVentanaCrearCuenta.lineEdit_correo.setText("")

        self.uiVentanaCrearCuenta.close()

















if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    #w.show()
    sys.exit(app.exec_())