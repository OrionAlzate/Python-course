global numA
global numB



menu = """
Bienvenido al menu principal, elija qué deseas hacer:

1 - Sumar
2 - Dividir
3 - Potenciación
4 - Multiplicar
5 - Raiz cuadrada
6 - Cambiar numeros introducidos
7 - Salir
"""
numA = int(input("Ingrese el primer número: "))

numB = int(input("Ingrese el segundo número: "))


OPCIONES = 0

while OPCIONES != 7:
    OPCIONES = int(input(menu))
    
    if OPCIONES == 1:
        suma = numA + numB
        print("\nEl resultado es: ", suma)
        
    elif OPCIONES == 2:
        dividir = numA / numB
        if numA == 0 or numB == 0:
            print("\nNo se puede dividir por cero")
        else:
            print("\nEl resultado es: ", dividir)

    elif OPCIONES == 3:
        potencia = numA ** numB
        print("\nEl resultado es: ", potencia)

    elif OPCIONES == 4:
        multiplicacion = numA * numB
        print("\nEl resultado es: ", multiplicacion)

    elif OPCIONES == 5:
        raiz_cuadradaA = numA ** (1/2)
        print("\nEl resultado es del primer numero es: ", raiz_cuadradaA)
        raiz_cuadradaB = numB ** (1/2)
        print("\nEl resultado es del segundo numero es: ", raiz_cuadradaB)

    elif OPCIONES == 6:
        cambiar_numeroA = int(input("Ingrese el nuevo primer número: "))
        cambiar_numeroB = int(input("Ingrese el nuevo segundo número: "))
        numA = cambiar_numeroA
        numB = cambiar_numeroB
        print("\nlos nuevos numeros son: ", numA,"Y", numB)
    elif OPCIONES == 7:
        print("\nGracias por usar el programa, adios.")
        break
    else:
        print("\nOpción inválida, intente nuevamente.")