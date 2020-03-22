def main():
    num1 = int(input('1° valor: '))
    num2 = int(input('2° valor: '))
    valores(num1, num2)


def valores(valor1, valor2):
    resto = valor1 % valor2
    soma = valor1 + valor2
    divisao  = valor1 / valor2

    if valor1 % valor2 == 1:
        print('A soma dos valores  mais o resto da divisão e: {} '.format(valor1 + valor2+resto))
    elif valor1 % valor2 == 2:
        if valor1 % 2 == 0:
            print('valor par: {}'.format(valor1))
        if valor2 % 2 == 0:
            print('valor par: {}'.format(valor2))
        if valor1 % 2 == 1:
            print('impar: {}'.format(valor1))
        if valor2 % 2 == 1:
            print('impar {}'.format(valor2))
    elif valor1 % valor2 == 3:
        print('a multiplicaçao dos valores e {}'.format(soma * valor1))
    elif valor1 % valor2 == 4:
        print('a divisão dos valores e {}'.format(divisao / valor2 != 0))
    else:
        print('o quadrado dos valores: {}, {}'.format(valor1**2, valor2**2))


main()
