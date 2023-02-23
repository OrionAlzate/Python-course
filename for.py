# contador = 1
# while contador < 1000:
#     print(contador)
#     # contador = contador + 1
#     contador += 1

#range es otro tipo de dato, en esre caso va del 0 al 1000
# for contador in range(10, 100): 
#     print(contador)

num = int(input("Ingresa un numero: "))
for i in range(10):
    tabla = num * i
    print(num,"X", i, "=" ,tabla)