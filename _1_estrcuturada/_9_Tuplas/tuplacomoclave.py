if __name__ == "__main__":
    diccionario = {
        ('id', 'int'):'2',
        'nombre':'Leo',
        'apellido':'Lopez'
    }

    #agregar tupla como clave
    diccionario[('Ana', 25)] = 'estudiante'
    diccionario[('Luis', 30)] = 'ingeniero'
    diccionario[('carlos', 40)] = 'abogado'


    ocupacion_ana = diccionario[('Ana', 25)]
    ocupacion_luis = diccionario[('Luis', 30)]

    print(f'la ocupacion de Ana es {ocupacion_ana}')
    print(f'la ocupacion de Luis es {ocupacion_luis}')