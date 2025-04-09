class auto:
    marca='honda'
    modelo=1000
    placa='PCH-96-04'


if __name__ == '__main__':
    taxi=auto()
    miauto=auto()

    print(taxi.placa)

    miauto.placa='TCV-963-12'
    print(miauto.placa)