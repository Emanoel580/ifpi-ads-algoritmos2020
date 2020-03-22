def main():
    num = int(input('numero de dois digitos: '))
    algarismo(num)


def algarismo(x):
    dezena = x // 10
    unidade = x % 10

    if dezena == unidade:
        print('o algarismo da dezena é igual ao algarismo da unidade!')
    else:
        print('diferentes !')


main()






