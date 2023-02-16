edad = int(input("Ingrese su edad: "))
pago = 0

if edad <= 10:
    pago = 0
    print("Puede entrar gratis")
elif edad >= 11 and edad <=18:
    pago = 24660
    print("Debe pagar: $" + str(pago))
elif edad >= 19:
    pago = 48000
    print("Debe pagar: $" + str(pago))
