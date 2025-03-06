if __name__ == "__main__":
    x = int(input('numero 1: '))
    y = int(input('numero 2: '))

    i: int = 1
    pot: int = 1

    while i < y:
        pot=pot*x
        i + 1

    print(f"El resultado de la multiplicacion es {pot}")