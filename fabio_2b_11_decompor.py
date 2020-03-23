def main():
    num = int(input('numero inteiro menor que 1000 ?:'))
    decompor(num)


def decompor(a):
    centena = a // 100
    resto = a % 100
    dezena = resto // 10
    unidade = resto % 10
    if a > 1000:
        print('numero invalido')
    else:
        print(f'{centena} centenas, {dezena} dezenas e {unidade} unidade')


main()