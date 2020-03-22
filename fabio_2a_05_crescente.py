def main():
    a = int(input('1° numero: '))
    b = int(input('2° numero: '))
    c = int(input('3° numero: '))
    ordem_crescente(a, b, c)


def ordem_crescente(x, y, z):
    if z > y > x:
        print(x, y, z)
    elif z > x > y:
        print(y, x, z)
    elif y > z > x:
        print(x, z, y)
    elif y > x > z:
        print(z, x, y)
    elif x > y > z:
        print(z, y, x)
    elif x > z > y:
        print(y, z, x)
    elif x == y == z:
        print('numeros iguais')
    else:
        print('dois numeros iguais')


main()







