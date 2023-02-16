desarrollo_software = float(input("Ingrese la nota de desarrollo de software: "))
matematicas = float(input("Ingrese la nota de matematicas: "))
logica = float(input("Ingrese la nota de logica de programación: "))


promedio = (matematicas + logica + desarrollo_software) / 3
promedio = round(promedio, 2)


if promedio >= 3:
    print("El promedio es: " , str(promedio), "APROBADO")

else:
    print("El promedio es: " , str(promedio), "REPROVADO")



