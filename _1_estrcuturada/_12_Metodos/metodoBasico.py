#def suma(a:int,b:int):
    #print(f'suma de {a} + {b} = {a+b}')
import statistics as mate
def suma(a:int,b=None, c=None):
    if b is None:
        print(f'suma de {a} + es {a}')
    else:
        if c is None:
            print(f'suma de {a} + {b} = {a+b}')
        else:
            print(f'suma de {a} + {b} + {c} = {a+b+c}')

def promedioArreglo(lista):
    lista.append(100)
    lista.append(200)
    lista.append(300)
    p=mate.mean(lista)
    print(f'el promedio es {p}')


if __name__ == "__main__":
    suma(100, 200)
    suma(3,6)
    suma(100, 200, 5)

    lista2=[1,2,3,4,5,6,7,8,9,10]
    promedioArreglo(lista2)
    print(lista2)