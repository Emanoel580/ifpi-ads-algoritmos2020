def main():
    angle = int(input('digite um angulo de 0 a 360: '))
    quadrante(angle)


def quadrante(valor1):
    if valor1 <= 90:
        print('o angulo {} pertence ao primeiro quadrante'.format(valor1))
    elif 90 < valor1 <= 180:
        print('o angulo {} pertence ao segundo quadrante'.format(valor1))
    elif 180 < valor1 <= 270:
        print('o angulo {} pertence ao terceiro quadrante'.format(valor1))
    elif 270 < valor1 <= 360:
        print('o angulo {} pertence ao quarto quadrante'.format(valor1))
    else:
        print('Por gentileza, digite o angulo dentre as opções acima!')


main()