
nombre = input("Ingrese su nombre: ")
horaEntrada = int(input("Ingrese la hora de llegada: "))
horaSalida = int(input("Ingrese la hora de salida: "))
valorHora = 2500
totalHoras = horaSalida - horaEntrada

 
print( nombre, "estuvo de", horaEntrada, "a", horaSalida, ".", " Su total de horas parqueado fue:" , totalHoras , "y su total a pagar es:", totalHoras * valorHora )