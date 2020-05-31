def main():
    num = int(input('1° valor: '))
    num2 = int(input('2° valor: '))
    print('-=' * 20)
    print('''Opções:
[ 1 ] Adição
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão''')
    opcao(num, num2)


def opcao(num, num2):

    print('-='*20)
    opcao = int(input('escola uma opçao: '))

    if opcao == 1:
        print('o resultado é:', num + num2)
    elif opcao == 2:
        print('o resultado é:', num - num2)
    elif opcao == 3:
        print('o resultado é:', num * num2)
    elif opcao == 4:
        print('o resultado é:', num // num2)
    else:
        print('A opção não corresponde com as opções disponiveis, por gentileza,'
         'tente novamente !')


main()

