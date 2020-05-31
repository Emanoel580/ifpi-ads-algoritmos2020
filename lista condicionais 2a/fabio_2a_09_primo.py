def main():
    num = int(input('numero: '))
    primo(num)


def primo(a):
    if a % 2 == 1:
        print('Este numero é Primo !')
    elif a == 2:
        print('Primo')
    elif a == 1:
        print(a, 'não e primo')
    else:
        print('Não e primo')


main()
