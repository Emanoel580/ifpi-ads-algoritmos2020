def main():
    num = float(input('numero: '))
    definir(num)


def definir(valor1):
    if valor1 // 1 == valor1:
        print(f' o numero {valor1} é inteiro')
    else:
        print(f'o numero {valor1} e decimal')


main()
