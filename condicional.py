#Programa que arroje mayor de edad, 
#si la edad es mayor o igual a 18, de lo contrario muestre 
#menor de edad

# edad = int(input("Ingrese su edad: "))

# if edad >= 18 and edad <=64 :
#     print("Usted es mayor de edad")
    
# elif edad >=65 :
#     print("usted pertenece a la tercera edad :)")
    
# else :
#     print("Usted es menor de edad")
    
# -------conducuinales---Platzi----------------

# edad = int(input("Ingrese su edad: "))
# if edad < 18:
#     # pass
#     print("eres menor de edad")
# else:
# # pass
#     if edad > 30:
#         print("eres mayor de edad")
    
        
numero = int(input("Ingrese un numero: "))
if numero < 5:
    print("Es menor a 5,", "El numero es:",numero)
elif numero >= 5 and numero <= 10:
    print("Está entre el 5 y el 10,", " ", "El numero es:",numero)
elif numero == 10:
    print("Es igual a 10,", "El numero es:",numero)
else:
    print("El numero es mayor a 10,", "El numero es:",numero)