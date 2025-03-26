if __name__ =="__main__":
    try:
        numero = int(input("dame un numero: "))
        resultado = 10 / numero

    except ValueError:
        print('el valor ingresado no es un numero')

    except ZeroDivisionError:
        print('no se puede dividir entre cero')

    else:
        print(f'el resultado es {resultado}')

    finally:
        print('fin del programa')
