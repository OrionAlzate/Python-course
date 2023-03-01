def run():
#     for contador in range(1001):
#         if contador %2 != 0:
#             continue
#         print(contador)
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)

    contador =0
    palabra = "Murcielagooooooooooo"

    while contador < len(palabra):
        contador += 1

        if contador == 5:
            continue

        if contador == 10:
            break
        
        print(contador)


if __name__ == '__main__':
    run()