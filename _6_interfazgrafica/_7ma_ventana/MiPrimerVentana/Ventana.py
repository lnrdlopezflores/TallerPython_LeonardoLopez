import sys
import mariadb
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QMessageBox


class Ventana(QMainWindow):
    def __init__(self, texto):
        super().__init__()
        uic.loadUi("ventana1.ui", self)
        self.btnNombre.clicked.connect(self.mostrarDatos)  # Changed to mostrarDatos
        self.texto = texto
        self.conexion = None  # Initialize connection variable

    def mostrarDatos(self):
        """Connects to the database, executes queries, and displays results."""
        try:
            self.conexion = mariadb.connect(
                host="localhost",
                database="almacen",
                user="root",
                password="",
                port=3306
            )
            print("Conexión a la base de datos exitosa")

            self.mostrarTabla("roles")
            self.mostrarTabla("usuarios")

        except mariadb.Error as error:
            QMessageBox.critical(self, "Error de Base de Datos", f"Error al conectar a la base de datos: {error}")
        finally:
            if self.conexion:
                self.conexion.close()
                print("Conexión cerrada")

    def mostrarTabla(self, tabla):
        """Displays data from a specified table."""
        try:
            cursor = self.conexion.cursor()
            consulta = f"SELECT * FROM {tabla}"
            cursor.execute(consulta)
            resultado = cursor.fetchall()

            # Dynamically determine column names and widths
            column_names = [i[0] for i in cursor.description]
            column_widths = [len(name) for name in column_names]
            for row in resultado:
                for i, value in enumerate(row):
                    column_widths[i] = max(column_widths[i], len(str(value)))

            # Print table header
            header_row = "| " + " | ".join([name.ljust(width) for name, width in zip(column_names, column_widths)]) + " |"
            print(header_row)
            print("|" + "-" * (len(header_row) - 2) + "|")

            # Print table rows
            for row in resultado:
                row_str = "| " + " | ".join([str(value).ljust(width) for value, width in zip(row, column_widths)]) + " |"
                print(row_str)

            print("|" + "-" * (len(header_row) - 2) + "|")
            print()  # Add a newline for better readability

        except mariadb.Error as error:
            QMessageBox.critical(self, "Error de Base de Datos", f"Error al consultar la tabla {tabla}: {error}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana("hola mundo")
    ventana.show()
    sys.exit(app.exec_())
