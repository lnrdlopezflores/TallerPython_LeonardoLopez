if __name__ == "__main__":
    nombre = str(input('ingresa el nombre 1: '))
    nombre2 = str(input('ingresa el nombre 2: '))

    if len(nombre) > len(nombre2):
        print(f'el nombre {nombre} es el mas largo')
    elif len(nombre) < len(nombre2):
        print(f'el nombre {nombre2} es el mas largo')
    else:
        if len(nombre) == len(nombre2):
            print(f'los nombres {nombre} y {nombre2} son iguales')