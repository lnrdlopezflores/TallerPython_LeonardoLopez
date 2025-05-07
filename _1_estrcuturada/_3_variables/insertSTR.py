if __name__ == '__main__':
    palabra: str = '%s'
    lista: list = ['nombre', 'apellido_paterno', 'Nombre_usuario', 'edad', 'correo_electronico']

    print(palabra)
    palabra= palabra * 5
    print(palabra)

    t=len(lista)
    print(t)

    palabra= palabra * len(lista)
    print(palabra)

    otrotexto=', '.join(lista)
    print(otrotexto)

    campos=', '.join(lista)
    print(campos)

    querySQL=f'INSERT INTO tabla({campos}) VALUES ({palabra})'
    print(querySQL)
