def main():
    num1 = int(input('1° numero: '))
    num2 = int(input('2° numero: '))
    num3 = int(input('3° numero: '))
    num4 = int(input('4° numero: '))
    num5 = int(input('5° numero: '))
    media(num1, num2, num3, num4, num5)


def media(valor1, valor2, valor3, valor4, valor5):
    total = (valor1 + valor2 + valor3 + valor4 + valor5) // 5
    print('a media equivale a: {}'.format(total))

    if valor1 > total:
        print('o valor {} e maior que a media'.format(valor1))
    if valor2 > total:
        print('o valor {} e maior que a media'.format(valor2))
    if valor3 > total:
        print('o valor {} e maior que a media'.format(valor3))
    if valor4 > total:
        print('o valor {} e maior que a media'.format(valor4))
    if valor5 > total:
        print('o valor {} e maior que a media'.format(valor5))


main()



