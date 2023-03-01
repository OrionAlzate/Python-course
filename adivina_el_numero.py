import random

def run():
    num_aleatorio = random.randint(1, 10)
    numero_elegido = int(input('Ingresa un numero del 1 al 10: '))
    while numero_elegido != num_aleatorio:
        if numero_elegido < num_aleatorio:
            print('Busca un numero mayor')
            numero_elegido = int(input("Elige otro número: "))

        elif numero_elegido > num_aleatorio:
            print('Busca un numero menor')
            numero_elegido = int(input("Elige otro número: "))
    print('Ganaste! en numero era:', numero_elegido)


if __name__ == '__main__':
    run()