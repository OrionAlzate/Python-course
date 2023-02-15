nombre = input("Escribe tu nombre: ")
# nombre = nombre.upper()
# print(nombre)
# nombre = nombre.capitalize()
# print(nombre)
# nombre = nombre.strip()
# print(nombre)
# nombre = nombre.replace('a','o')
# print(nombre)
# letra = nombre[0].capitalize()
# print(letra)
# print(len(nombre))

medioNombre = nombre[0:5] #para hacer un slice (rebanadas)
apellido = nombre[6:12]
print(medioNombre)
print(apellido)

otroSlice = nombre[::2] # el tercer parametro define los saltos que va a tener
print(otroSlice)