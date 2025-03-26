def ciclo(vueltas):
    i: int = 0
    while i < vueltas:
        i+=1
        yield i

    return i

if __name__ == "__main__":
    for valor in ciclo(5):
        print({valor})