import random
if __name__ == "__main__":

    #integrantes equipo:
    #Leonardo Lopez Flores

    num = int(random.randint(1, 100))
    intentos = 0
    max_intentos = 10

    print('Bienvenido al juego: adivina el numero!')

    while intentos < max_intentos:

        intento = int(input(f'intento {intentos+1}/{max_intentos} dame un numero: '))

        if intento < 1 or intento > 100:
            print("Por favor, ingresa un número dentro del rango (1-100).")
            continue

        intentos += 1 

        if intento < num:
            print("El número es mayor. ¡Sigue intentando!")
        elif intento > num:
            print("El número es menor. ¡Sigue intentando!")
        elif num == intento:
            print(f"¡Felicidades! Has adivinado el número {num} en {intentos} intentos.")
            break

    if intento != num:
        print(f"Lo siento, has agotado tus {max_intentos} intentos. El número era {num}.")