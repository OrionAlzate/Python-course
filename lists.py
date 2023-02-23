ensaladaDeFrutas = ["manzana", "mango", "banano", "yogurt", "queso", "helado", "fresa"]


# for ingrediente in ensaladaDeFrutas: # recorrido de la lista por ciclo FOR IN
#     print(ingrediente.upper())


# print(ensaladaDeFrutas[:4]) # devuelve una lista hasta el index indicado
# print(ensaladaDeFrutas[3]) # devuelve solo el index indicado
# print(ensaladaDeFrutas[4:]) # devuelve desde el index indicado hasta el final de la lista
# print(ensaladaDeFrutas[-1]) # empieza a contar desde del último index para atras [-2] muestra el penultimo, etc.
# print(ensaladaDeFrutas[-3:]) 


# ---------------
# verificar por un if si hay un elemento dentro de una lista
# fruta = input('que ingrediente en la ensalada de frutas?: ')
# if fruta in ensaladaDeFrutas:
#     print(fruta+ ' si esta incluido en la ensalada de frutas')
# else:
#     print(fruta+' no esta incluido en la ensalada de frutas')


# ---------------
# Cambiar un valor de un index en una lista
ensaladaDeFrutas[3] = "granola"
print(ensaladaDeFrutas)

# Cambiar un valor de un rango en una lista
ensaladaDeFrutas[2:4] = ["sandia","kiwi"] 
print(ensaladaDeFrutas)

