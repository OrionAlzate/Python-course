edad = int(input("Ingrese su edad: "))


if edad >= 18:
    ingresos = int(input("Ingrese el valor de sus ingresos: "))
    if ingresos >= 2500000:
        print("puede tributar")
    elif ingresos < 2500000:
        print("no tiene ingresos suficientes")
else:
    print("Aun es menor de edad")

