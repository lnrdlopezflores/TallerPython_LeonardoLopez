if __name__ == '__main__':
    x=int(input('numero 1: '))
    y=int(input('numero 2: '))

    i:int=1
    suma:int=1

    while i<y:
        suma *= x
        i = i + 1

    print(f"El resultado de la multiplicacion es {suma}")