def main():
    a = int(input('1° numero:'))
    b = int(input('2° numero: '))
    c = int(input('3° numero: '))
    maior_num(a, b, c)


def maior_num(x, y, z):
    if z > y and y > x:
        print('o maior numero é {}'.format(z))
    elif y > z and z > x:
        print('o maior  numero é {}'.format(y))
    elif x > y and  y > z:
        print('o maior numero é {}'.format(x))
    else:
        print('numeros iguais !')


main()