if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    listaImpares=list(filter(lambda num: num % 2 == 0, numeros))
    ListaPares=list(filter(lambda num: num % 2 == 1, numeros))

    print(f'numeros impares: {listaImpares}')
    print(f'numeros pares: {ListaPares}')

    ListaImparesConPotencia= list(map(lambda z:z**2, filter(lambda t: t%2==1, numeros)))
