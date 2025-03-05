if __name__ == "__main__":
    a=  int(input("proporciona un numero: "))
    b = int(input("proporciona otro numero: "))
    c = int(input("proporciona un ultimo numero: "))

    if a>b:
        if a>c:
            print(f'el mayor es{a}')
        else:
            print(f'el mayor es{c}')
    else:
        if b>c:
            print(f'el mayor es{b}')
        else:
            print(f'el mayor es{c}')