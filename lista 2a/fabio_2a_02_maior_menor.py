def main():
     a = int(input('1° numero: '))
     b = int(input('2° numero:'))
     menor_maior(a, b)


def menor_maior(x, y):
    if x == y:
        print('iguais')
    elif x > y:
        print('o primeiro n° {} é maior do que {} '.format(x,y))
    else:
        print('o segundo n° {} é  maior do que {}'.format(y, x))


main()
