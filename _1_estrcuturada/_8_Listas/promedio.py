import statistics as mate

if __name__ == '__main__':
    numeros=[10,20,30,50,60,80,90,30,40]

    conteo = 1
    suma = 0
    promedio = 0

    for valor in numeros:
        suma += valor
        conteo += 1

    promedio=suma/conteo
    print(promedio)

    print('')

    #opcion medio lenta
    suma =0
    for valor in numeros:
        suma += valor
    promedio=suma/len(numeros)
    print(promedio)

    print('')
    #Metodo rapido
    promedio=mate.mean(numeros)
    print(promedio)