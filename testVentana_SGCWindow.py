import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from ventana_SGC import Ui_ventana_SGC
from ventana_realizar_consulta import Ui_ventana_realizar_consulta
from ventana_registrar_movimiento import Ui_ventana_registrar_movimiento
import sqlite3

class ventanaRegistrarMovimiento(qtw.QWidget, Ui_ventana_registrar_movimiento):
    def __init__(self):
        super().__init__()


class ventanaRealizarConsulta(qtw.QWidget, Ui_ventana_realizar_consulta):
    def __init__(self):
        super().__init__()


class MainWindowSGC(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Your code will go here
        self.uiSGC = Ui_ventana_SGC()
        self.uiSGC.setupUi(self)
        self.setGeometry(qtc.QRect(800, 250, 0, 0))

        # Si clickeamos en el boton de Salir, llamamos a la funcion boton_salir()
        self.uiSGC.pushButton_salir.clicked.connect(self.boton_salir)
        # Si usamos el metodo "setAutoDefault(True)" en un boton, este emitira la señal de "clicked" cuando presionemos enter
        self.uiSGC.pushButton_salir.setAutoDefault(True)

        self.uiSGC.pushButton_realizarConsultas.clicked.connect(self.ventana_realizar_consulta)

        self.uiSGC.pushButton_registrarMovimientos.clicked.connect(self.ventana_registrar_movimientos)

        # Your code ends here
        self.show()

    def boton_salir(self):
        self.close()

    def ventana_realizar_consulta(self):
        self.uiVentanaRealizarConsulta = ventanaRealizarConsulta()
        self.uiVentanaRealizarConsulta.setupUi(self.uiVentanaRealizarConsulta)
        conexion = sqlite3.connect('registrarMovimiento.bd')
        cursor = conexion.cursor()

        try:
            datos_bd = cursor.execute("SELECT * FROM movimientos").fetchall()

            for datos in datos_bd:
                self.uiVentanaRealizarConsulta.listWidget.addItem("Monto: {} - Tipo de movimiento: {}".format(datos[1], datos[2]))

        except sqlite3.OperationalError:
            qtw.QMessageBox.information(self, "No hay nada", "Primero debe registrar algunos movimientos!")

        conexion.close()

        self.uiVentanaRealizarConsulta.show()

    def ventana_registrar_movimientos(self):
        self.uiVentanaRegistrarMovimiento = ventanaRegistrarMovimiento()
        self.uiVentanaRegistrarMovimiento.setupUi(self.uiVentanaRegistrarMovimiento)

        # Al presionar el boton de Registrar movimiento de la ventana Registrar Movimiento guardará los datos en una base de datos local.
        self.uiVentanaRegistrarMovimiento.pushButton_registrarMovimiento.clicked.connect(self.registrar_movimiento)
        self.uiVentanaRegistrarMovimiento.pushButton_registrarMovimiento.setAutoDefault(True)

        #Al presionar el boton de salir de la ventana de Registrar movimiento se cierra la misma.
        self.uiVentanaRegistrarMovimiento.pushButton_salir.clicked.connect(self.uiVentanaRegistrarMovimiento.close)
        self.uiVentanaRegistrarMovimiento.pushButton_salir.setAutoDefault(True)

        #Muestra la ventana de registrar movimiento
        self.uiVentanaRegistrarMovimiento.show()

    def registrar_movimiento(self):
        conexion = sqlite3.connect('registrarMovimiento.bd')
        cursor = conexion.cursor()

        monto = self.uiVentanaRegistrarMovimiento.lineEdit_monto.text()
        tipo = self.uiVentanaRegistrarMovimiento.lineEdit_tipoMovimiento.text()

        if monto == '' or tipo == '':
            monto = None
            tipo = None

        datos_movimiento = [(monto, tipo)]

        try:
            cursor.execute("""CREATE TABLE movimientos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            monto FLOAT NOT NULL,
                            tipo VARCHAR(50) NOT NULL)""")

        except sqlite3.OperationalError:
            pass

        try:
            cursor.executemany("INSERT INTO movimientos VALUES (NULL, ?, ?)", datos_movimiento).fetchall()
        except sqlite3.IntegrityError:
            qtw.QMessageBox.information(self, "No se pudo registrar", "Asegurese de llenar correctamente todos los campos, si el problema persiste, es posible que haya ingresado el monto en un formato incorrecto.")
            self.uiVentanaRegistrarMovimiento.close()

        conexion.commit()
        conexion.close()

        #limpiamos el contenido de los "Line Edit"
        self.uiVentanaRegistrarMovimiento.lineEdit_monto.setText("")
        self.uiVentanaRegistrarMovimiento.lineEdit_tipoMovimiento.setText("")


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindowSGC()
    sys.exit(app.exec_())
