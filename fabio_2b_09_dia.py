def main():
    num = int(input('dia: '))
    dia(num)


def dia(a):
    if a == 1:
        print('Domingo !')
    elif a == 2:
        print('Segunda !')
    else:
        print('valor invalido !')


main()
