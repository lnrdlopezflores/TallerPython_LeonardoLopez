if __name__ == "__main__":
    mi_lista=[1,2,3]
    mi_lista.append(4)
    print(mi_lista)

    mi_lista=[1,2,3]
    otra_lista=[4,5,6]
    mi_lista.extend(otra_lista)
    print(mi_lista)

    mi_lista=[1,2,3]
    mi_lista.insert(1,4)
    print(mi_lista)

    mi_lista=[1,2,3]
    mi_lista.remove(2)
    print(mi_lista)

    mi_lista=[1,2,3]
    elemento=mi_lista.pop(1)
    print(mi_lista)
    print(elemento)

    mi_lista=[1,2,3,2]
    indice=mi_lista.index(2)
    print(indice)

    mi_lista=[1,2,3,2]
    contador=mi_lista.count(2)
    print(contador)

    mi_lista=[3,1,4,2]
    mi_lista.sort()
    print(mi_lista)

    mi_lista.sort(reverse=True)
    print(mi_lista)

    mi_lista=[1,2,3,4]
    mi_lista.reverse()
    print(mi_lista)

    mi_lista=[1,2,3,4]
    mi_lista.clear()
    print(mi_lista)

    mi_lista=[1,2,3,4]
    copia=mi_lista.copy()
    mi_lista.append(5)
    print(copia)

    