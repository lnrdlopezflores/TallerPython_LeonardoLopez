import json

if __name__ == "__main__":
    with (open("datos.json", "r", encoding="utf-8") as archivo):
        datos = json.load(archivo)


    for persona in datos["personas"]:
        print("nombre: ", persona["nombre"])
        print("edad: ", persona["edad"])
        print("ciudad: ", persona["ciudad"])
        print("estado: ", persona["estado"])
        print(" ")