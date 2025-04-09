import json
import sys

# Definir colores ANSI
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"


def cargar_json(archivo):

    try:
        file = open(archivo, 'r', encoding='utf-8')
        datos = json.load(file)
        return datos.get("tabla", [])

    except FileNotFoundError:
        print(f"{RED}Error al cargar el archivo JSON:{RESET}")
        return []
    except json.decoder.JSONDecodeError:
        print(f"{RED}Error al cargar el archivo JSON:{RESET}")
        return []
    except Exception as e:
        print(f"{RED}Error al cargar el archivo JSON: {e}")
    else:
        file.close()
        print(RESET, 'cerrado')


def iterar_usuarios(usuarios):
    for usuario in usuarios:
        yield usuario


def imprimir_tabla(tabla):
    print("+----+----------------+-------+-------------------+----------------+")
    print(f"| {'ID':<2} | {'Nombre':<14} | {'Edad':<5} | {'RFC':<17} | {'Estado':<14} |")
    print("+----+----------------+-------+-------------------+----------------+")

    for i, fila in enumerate(tabla, start=1):
        match i:
            case 1:
                sys.stdout.write(RED)
            case 2:
                sys.stdout.write(WHITE)
            case 3:
                sys.stdout.write(GREEN)
            case 4:
                sys.stdout.write(MAGENTA)
            case 5:
                sys.stdout.write(YELLOW)
            case _:
                sys.stdout.write(RESET)

        print(f"| {fila[0]:<2} | {fila[1]:<14} | {fila[2]:<5} | {fila[3]:<17} | {fila[4]:<14} |{RESET}")

    print("+----+----------------+-------+-------------------+----------------+")


if __name__ == "__main__":
    archivo = "tablaaa.json"
    usuarios = cargar_json(archivo)

    tabla = []
    for usuario in iterar_usuarios(usuarios):
        if all(key in usuario for key in ["id", "Nombre", "Edad", "RFC"]):  # Verificación de claves
            estado = "Mayor de edad" if usuario["Edad"] >= 18 else "Menor de edad"
            tabla.append([usuario["id"], usuario["Nombre"], usuario["Edad"], usuario["RFC"], estado])
        else:
            print(f"{YELLOW}Advertencia: Datos faltantes en {usuario}{RESET}")

    if tabla:
        imprimir_tabla(tabla)
    else:
        print(f"{RED}No hay datos para mostrar.{RESET}")