numA = int(input("Ingrese un numero para crear la tabla de multiplicar: "))

# contador = 0
# while contador < numA:
#     resultado = numA * contador
#     contador = contador + 1
#     print(numA, "*", contador, "=", resultado)

for i in range(numA):
    resultado = numA * i
    print(numA, "*", i, "=", resultado)
