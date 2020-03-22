def main():
    print('escolha uma opção: ')
    print('''
    [ 1 ]
    [ 2 ]
    [ 3 ]''')
    opcao(1, 2, 3)


def opcao(num, num2, num3):
    print('-='*10)
    opcao = int(input('escolha uma opção: '))
    if opcao == num:
        print(num)
    elif opcao == num2:
        print(num2)
    elif opcao == num3:
        print(num3)
    else:
        print('Opção invalida, tente novamente com as opções acima')


if __name__ == '__main__':
    main()

