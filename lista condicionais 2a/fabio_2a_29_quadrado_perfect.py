def main():
    num = int(input('digite numero de 4 digitos: '))
    quadrado(num)


def quadrado(valor1):
    raiz = valor1 ** 0.5
    if raiz ** 2 == valor1:
        print(f'o numero {valor1} e quadrado perfeito')
    else:
        print('não e quadrado perfeito')


main()
