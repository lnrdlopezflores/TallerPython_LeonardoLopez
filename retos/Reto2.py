#integrantes equipo:
#LEonardo Lopez Flores

def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ").strip()
    cantidad_prod = input("Ingrese la cantidad del producto: ").strip()

    if not cantidad_prod.isdigit():
        print("La cantidad debe ser un número entero.")
        return
    cantidad = int(cantidad_prod)

    for producto in inventario:
        if producto[0].lower() == nombre.lower():
            producto[1] += cantidad
            print(f"Se actualizó el stock de {nombre} a {producto[1]}.")
            return

    inventario.append([nombre, cantidad])
    print(f"Producto {nombre} agregado con cantidad {cantidad}.")

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\nInventario Actual:")
    for producto in inventario:
        print(f"Producto: {producto[0]}, Cantidad: {producto[1]}")
    print()

def vender_producto(inventario):
    if not inventario:
        print("No hay productos en el inventario para vender.")
        return

    nombre = input("Ingrese el nombre del producto a vender: ").strip()
    for i, producto in enumerate(inventario):
        if producto[0].lower() == nombre.lower():
            print(f"Producto {producto[0]} vendido.")
            inventario.pop(i)
            return
    print(f"El producto {nombre} no se encontró en el inventario.")

def menu():
    inventario = []
    while True:
        print("Inventario Básico")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender producto")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            vender_producto(inventario)
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()