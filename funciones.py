# def mostrarTexto():
#     print("Mensaje especial")
#     print("Estoy aprendiendo a usar funciones ")


# mostrarTexto()
def conversacion(mensaje):
    print('Hola')
    print('Como estás')
    print(mensaje)
    print('Adios')



opcion = int(input("Elija una opcion (1,2,3): "))

if opcion == 1:
    conversacion("Elejiste la opción 1")
elif opcion == 2:
    conversacion("Elejiste la opción 2")
elif opcion == 3:
    conversacion("Elejiste la opción 3")
else: 
    print("Debes elejir la opcion correcta")
    