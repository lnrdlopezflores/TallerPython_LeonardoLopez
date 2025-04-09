# Clase Libro
class Libro:
    def __init__(self, isbn, titulo, autor):
        self.__isbn = isbn       # Atributo privado
        self.__titulo = titulo   # Atributo privado
        self.__autor = autor     # Atributo privado

    # Getters
    def get_isbn(self):
        return self.__isbn

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor


# Clase ColeccionLibros
class ColeccionLibros:
    def __init__(self):
        self.libros = []

    def add(self, libro):
        self.libros.append(libro)
        print("Libro agregado correctamente.")

    def delete(self, isbn):
        for libro in self.libros:
            if libro.get_isbn() == isbn:
                self.libros.remove(libro)
                print("Libro eliminado correctamente.")
                return
        print("Libro no encontrado.")

    def show(self):
        if not self.libros:
            print("No hay libros registrados.")
            return
        for libro in self.libros:
            print(f"ISBN: {libro.get_isbn()}, Título: {libro.get_titulo()}, Autor: {libro.get_autor()}")


if __name__ == "__main__":
    coleccion = ColeccionLibros()

    # Crear algunos libros
    libro1 = Libro("978-84-376-0494-7", "Cien años de soledad", "Gabriel García Márquez")
    libro2 = Libro("978-3-16-148410-0", "El Principito", "Antoine de Saint-Exupéry")
    libro3 = Libro("978-43-26-158420-6", "Don Quijote de la mancha", "Miguel de Cervantes Saavedra")
    libro4 = Libro("978-3-16-148412-4", "El Principito", "Antoine de Saint-Exupéry")
    libro5 = Libro("978-333-76-158470-3", "La odisea", "Homero")

    # Agregar libros
    coleccion.add(libro1)
    coleccion.add(libro2)
    coleccion.add(libro3)
    coleccion.add(libro4)
    coleccion.add(libro5)

    # Mostrar todos los libros
    print("\nLista de libros:")
    coleccion.show()

    # Eliminar un libro por ISBN
    print("\nEliminando libro con ISBN 978-3-16-148410-0:")
    coleccion.delete("978-3-16-148410-0")

    # Mostrar libros nuevamente
    print("\nLista de libros actualizada:")
    coleccion.show()