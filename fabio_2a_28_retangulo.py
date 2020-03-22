def main():
    x = float(input('coordenada de x: '))
    y = float(input('coordenada de y: '))
    coordenada(x, y)


def coordenada(valor1, valor2):
    area_retangulo = valor1 * valor2
    if area_retangulo > 0:
        print('a area do retangulo é: {}'.format(area_retangulo))
    elif area_retangulo == 0:
        print('digite coordenadas validas')
    else:
        print('não pode ser negativo')


main()
