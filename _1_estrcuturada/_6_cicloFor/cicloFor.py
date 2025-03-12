import sys

if __name__ == '__main__':
    for i in range(10):
        print(f"{i}")

    print("")
    print("6 a 12")

    for i in range(6, 12):
        print(f"{i}")

    print("")
    print("rengo del 6 a 11 pero con incremento")
    for i in range(6, 12, 3):
        print(f"{i}")

    for j in range(1, 20):
        print(f"{j}", end=" ")

    sys.stdout.write("texto sin salto de linea")