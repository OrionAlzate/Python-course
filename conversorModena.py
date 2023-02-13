eleccion = int(input("""
Elija modena a convertir de pesos a:
1- AUD,
2- USD,
3- CAD,
4- GBP:

Elije una opción: """))
monto = int(input("Ingrese el monto en COP (Pesos colombianos) a convertir: "))


if eleccion == 1:
    result = monto / 3351
    print("Su valor es: $" ,round(result, 2), "(AUD)")
elif eleccion == 2:
    result = monto / 4810
    print("Su valor es: $" ,round(result, 2), "(USD)")
elif eleccion == 3:
    result = monto / 3607
    print("Su valor es: $" ,round(result, 2), "(CAD)")
elif eleccion == 4:
    result = monto / 5838
    print("Su valor es: $" ,round(result, 2), "(GBP)")
else :
    print("Eligió otra opción, debe elejir las opciones indicadas.")