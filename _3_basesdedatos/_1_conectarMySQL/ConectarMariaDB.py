import mariadb

def conectar_y_consultar():
    try:
        conexion = mariadb.connect(
            host="localhost",
            database="almacen",
            user="root",
            password="",
            port=3306
        )
        print(type(conexion))
        print("conexion a la base de datos Ounus")

        cursor0 = conexion.cursor()
        consulta = "select * from roles"
        cursor0.execute(consulta)
        resultado = cursor0.fetchall()
        print("datos de la tabla: roles")
        print(
            '+----------------------------+')
        print(
            f'| {"ID":<3} | {"Nombre":<20} |')
        print(
            '+----------------------------+')

        for fila in resultado:
            print(f'| {fila[0]:<3} | {fila[1]:<20} |')
            print(
                '+----------------------------+')

        cursor = conexion.cursor()
        consulta = "select * from usuarios"
        cursor.execute(consulta)

        resultado = cursor.fetchall()
        print('')
        print('')
        print('')
        print("datos de la tabla: usuarios")
        print(
            '+--------------------------------------------------------------------------------------------------------------+')
        print(
            f'| {"ID":<3} | {"Nombre":<20} | {"Usuario":<15} | {"Correo Electrónico":<30} | {"Contraseña":<15} | {"Rol":<10} |')
        print(
            '+--------------------------------------------------------------------------------------------------------------+')

        for fila in resultado:
            print(f'| {fila[0]:<3} | {fila[1]:<20} | {fila[2]:<15} | {fila[3]:<30} | {fila[4]:<15} | {fila[5]:<10} |')
            print(
                '+--------------------------------------------------------------------------------------------------------------+')

    except mariadb.Error as error:
        print(f"Error con base de datos: {error}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
            print("conexion cerrada")

if __name__ == '__main__':
    conectar_y_consultar()