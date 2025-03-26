# funcion que recibe la tupla
def calcular_area(rectangulo: tuple[int, int]) -> int:
    largo, ancho = rectangulo
    return largo * ancho

def cuadrado(rectangulo: tuple[int, int]) -> int:
    largo, ancho = rectangulo
    largo = largo * largo
    ancho = ancho * ancho
    return (largo, ancho)
if __name__ == "__main__":

    #crear la tupla
    dimensiones = (10, 5)

    #llamar a la funcion con la tupla
    area = calcular_area(dimensiones)

    print(f'el area del rectangulo es: {area} mts. cuadrados')

    largo, ancho = cuadrado((5, 3))