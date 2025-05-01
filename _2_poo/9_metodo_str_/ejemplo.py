
class DatosPersonales:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __getstate__(self):
        return self.nombre;

    def getApelido(self):
        return self.apellido;

    def __getnewargs__(self):
        return self.edad;

    def corto(self):
        return self.nombre+''+ self.apellido+''+ self.edad;

    def __str__(self):
        return self.nombre+''+ self.apellido+''+ self.edad;


if __name__ == '__main__':
    datos= DatosPersonales('leonardo', 'lopez', '23')

    print(datos)

