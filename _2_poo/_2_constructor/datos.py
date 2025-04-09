class Datos:
    def _init_(self, nombre, correo, whatsapp):
        self.nombre = nombre
        self.correo = correo
        self.whatsapp = whatsapp

    def setNombre(self,nombre:str):
        self.nombre=nombre


if __name__ == 'main':
    datos=Datos('Edwin','darienedwin@gmail.com','5577354435')

    print(datos.nombre)
    datos.setNombre("Juan")
    print(datos.nombre)
    datos.nombre="Gabriela"
    print(datos.nombre)