class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = {}

    def agregar_libro(self, titulo, autor, genero, copias):
        libro = {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "copias": copias
        }
        self.libros.append(libro)
        print(f'Libro "{titulo}" agregado con éxito.')

    def buscar_libros(self, **criterios):
        for libro in self.libros:
            if all(libro[key] == value for key, value in criterios.items() if key in libro):
                yield libro

    def prestar_libro(self, usuario, titulo):
        for libro in self.libros:
            if libro["titulo"].lower() == titulo.lower() and libro["copias"] > 0:
                libro["copias"] -= 1
                self.usuarios.setdefault(usuario, []).append(titulo)
                print(f'Libro "{titulo}" prestado a {usuario}.')
                return
        print(f'No hay copias disponibles de "{titulo}".')

    def devolver_libro(self, usuario, titulo):
        if usuario in self.usuarios and titulo in self.usuarios[usuario]:
            for libro in self.libros:
                if libro["titulo"].lower() == titulo.lower():
                    libro["copias"] += 1
                    self.usuarios[usuario].remove(titulo)
                    print(f'Libro "{titulo}" devuelto por {usuario}.')
                    return
        print(f'{usuario} no tiene el libro "{titulo}" prestado.')

    def mostrar_libros_disponibles(self):
        for libro in self.libros:
            if libro["copias"] > 0:
                print(f'{libro["titulo"]} - {libro["autor"]} ({libro["genero"]}) - Copias: {libro["copias"]}')



if __name__ == "__main__":
    biblioteca = Biblioteca()
    while True:
        print("\n1. Agregar libro")
        print("2. Buscar libros")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Mostrar libros disponibles")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            copias = int(input("Número de copias: "))
            biblioteca.agregar_libro(titulo, autor, genero, copias)

        elif opcion == "2":
            criterio = input("Buscar por (titulo/autor/genero): ")
            valor = input(f"Ingrese el {criterio}: ")
            libros_encontrados = list(biblioteca.buscar_libros(**{criterio: valor}))
            if libros_encontrados:
                for libro in libros_encontrados:
                    print(libro)
            else:
                print("No se encontraron libros.")

        elif opcion == "3":
            usuario = input("Nombre de usuario: ")
            titulo = input("Título del libro: ")
            biblioteca.prestar_libro(usuario, titulo)

        elif opcion == "4":
            usuario = input("Nombre de usuario: ")
            titulo = input("Título del libro: ")
            biblioteca.devolver_libro(usuario, titulo)

        elif opcion == "5":
            biblioteca.mostrar_libros_disponibles()

        elif opcion == "6":
            break

        else:
            print("Opción no válida. Intente nuevamente.")
