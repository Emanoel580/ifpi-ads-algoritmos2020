def main():
    num = int(input('numero: '))
    sinal(num)


def sinal(valor1):
    if valor1 > 0:
        print('Positivo !')
    elif valor1 == 0:
        print(' o numer zero é neutro')
    else:
        print('Este numero é negativo !')


main()
