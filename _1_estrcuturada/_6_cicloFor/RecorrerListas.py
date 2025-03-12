if __name__ == '__main__':
    lista=[1, 2, 3,'lunes', 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    lista.append(200)
    lista.append("viernes")
    lista.append(False)
    lista.append(2.69)
    lista.append('leo')

    lista2=[1200, 1300, 1500]

    lista.append(lista2)

    for elemento in lista:
        print(elemento)

    lista2=[17, 18, 19, 20]
    lista.extend(lista2)


    nombre:str
    nombre = 'leonardo'
    nombre += ' lopez'
    print(nombre)

    lista3 = ['federico', 'pablo', 'karla']
    cadena:str =' - '.join(lista3)


