def main():
    num = int(input('digite n° de 1000 a 9999: '))
    digito(num)


def digito(valor1):
    num1 = valor1 // 100
    num2 = valor1 % 100
    num_total = num1 + num2
    raiz = (num_total ** 2)
    if valor1 == raiz:
        print(raiz)
    else:
        print('não possui as condições necessárias')


main()
