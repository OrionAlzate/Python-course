def palindromo(palabra):
        palabra = palabra.replace(' ', '') #reemplazando los espacios por un strign vacio
        palabra = palabra.lower() #toda la frase en minuscula
        palabra_invertida = palabra[::-1] #recorrido de la frase en reversa
        print('"',palabra_invertida,'"')
        if palabra == palabra_invertida:
            return True
        else:
            return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()