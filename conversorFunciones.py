def conversor(tipo_pesos, valor_dolar):
    pesos = input('Cuantos pesos ' + tipo_pesos + 'tiene?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $ ' + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 🪙

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elija una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 4829)
elif opcion == 2:
    conversor("argentinos", 192)

elif opcion == 3:
    conversor("mexicanos", 18)
else:
    print('Debe escoger una de las opciones.')