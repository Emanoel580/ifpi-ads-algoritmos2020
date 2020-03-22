def main():
    lado1 = float(input('diga o 1° lado: '))
    lado2 = float(input('diga o 2° lado: '))
    lado3 = float(input('diga o 3° lado: '))
    triangulo(lado1, lado2, lado3)


def triangulo(valor1, valor2, valor3):
    if valor1 > valor2 and valor1 > valor3:
        print('A hipotenusa e {}, e os catetos: {} e  {}'.format(valor1, valor2, valor3))
    elif valor2 > valor1 and valor2 > valor3:
        print('A hipotenusa  e {}, e os catetos: {} e {}'.format(valor2, valor1, valor3))
    elif valor3 > valor2 and valor3 > valor1:
        print('A hipotenusa e {}, e os catetos: {} e {}'.format(valor3, valor2, valor1))
    else:
        print('Valores indevidos')


main()
