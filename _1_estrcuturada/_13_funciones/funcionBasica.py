def suma(a:int,b:int)->int:
    return a+b
def sumaArreglo(lista:list)->int:
    return sum(lista)

if __name__ == "__main__":
    print(f'la suma es {suma(1,2)}')

    lista=[1,2,3,4,5]
    print(f'la suma de un arreglo es {sumaArreglo(lista)}')