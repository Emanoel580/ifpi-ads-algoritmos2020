def main():
    num = float(input('numero: '))
    valor_arredondado(num)


def valor_arredondado(valor1):
    num2 = valor1 % 1
    num_acima = valor1 // 1 + 1
    num_abaixo = valor1 - num2
    if num2 >= 0.5:
        print(num_acima)
    elif num2 < 0.5:
        print(num_abaixo)
    else:
        print('numero digitado não e fracionario')


main()
