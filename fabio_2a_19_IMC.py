def main():
    peso = int(input('peso: '))
    altura = float(input('altura: '))
    IMC(peso, altura)


def IMC(valor1, valor2):
    imc = valor1 / valor2 ** 2
    if imc < 25:
        print('o indice de massa corporea é de {:.2f}, esta NORMAL '.format(imc))
    elif imc > 30:
        print('o indice de massa corporea é de {:.2f}, possui OBESIDADE MORBIDA '.format(imc))
    else:
        print('o indice de massa corporea é de {:.2f}, esta OBESO'.format(imc))


if __name__ == '_main_':
    main()


