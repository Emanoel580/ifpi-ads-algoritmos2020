def main():
    a = float(input('Coeficiente A da equação: '))
    b = float(input('Coeficiente B da equação: '))
    c = float(input('Coeficiente C da equação: '))
    equacao(a, b, c)


def equacao(val_1, val_2, val_3):
    delta = (val_2 ** 2) - 4 * val_1 * val_3
    raiz_1 = (-val_2 + (delta ** 0.5)) / 2 * val_1
    raiz_2 = (-val_2 - (delta ** 0.5)) / 2 * val_1
    if delta >= 0:
        print('O valor da raiz 1 é {} e o valor da raiz 2 é {}'.format(raiz_1, raiz_2))
    else:
        print('Não foi possível definir pois delta é menor que zero')


main()
