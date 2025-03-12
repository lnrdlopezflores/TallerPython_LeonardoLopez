from unittest import case

if __name__ == '__main__':
    n = int(input('numero de nombres: '))

    indios = [0,0,0,0,0,0,0,0,0,0]
    extras = int(1)

    for i in range(n):
        nombre = str(input('nombre: '))
        tam=len(nombre)

        match tam:
            case 1: indios[0] += 1
            case 2: indios[1] += 1
            case 3: indios[2] += 1
            case 4: indios[3] += 1
            case 5: indios[4] += 1
            case 6: indios[5] += 1
            case 7: indios[6] += 1
            case 8: indios[7] += 1
            case 9: indios[8] += 1
            case 10: indios[9] += 1
            case _: extras += 1
    i:int=1
    for elemento in indios:
        print(f'el total de nombres de {i} letras es: {elemento}')
        i += 1
    print(f'el total de nombres de mas de 10 letras es: {extras}')
