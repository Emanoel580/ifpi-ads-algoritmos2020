def main():
    num = int(input('numero: '))
    par_impar(num)


def par_impar(num1):
        if num1 % 2 == 0 or num1 == 0:
            print('numero par')
        elif num1 == 1:
            print('impar !')
        else:
            print('impar !')


main()