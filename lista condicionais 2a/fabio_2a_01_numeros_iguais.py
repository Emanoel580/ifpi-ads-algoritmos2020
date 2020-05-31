def main():
    a = int(input('1° numero: '))
    b = int(input('2 numero: '))
    c = int(input('3 numero: '))
    num_igual(a, b, c)


def num_igual(num, num_2, num_3):

    if num == num_2 and num_2 == num_3:
        print('valores são iguais')
    elif num == num_2:
                print('o primeiro n° e o segundo são iguais')
    elif num_2 == num_3:
                print('o segundo n° e o terceiro são iguias')
    elif num == num_3:
                print('o primeiro n° e o terceiro são iguais')
    else:
        print('os n° são diferentes !')


main()











