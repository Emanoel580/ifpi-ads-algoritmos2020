def main():
    produto1 = float(input('1° produto: '))
    produto2 = float(input('2° produto: '))
    produto3 = float(input('3° produto: '))
    produtos(produto1, produto2, produto3)


def produtos(valor1, valor2, valor3):
    menor = valor1
    if valor2 < menor:
        menor = valor2
    if valor3 < menor:
        menor = valor3
    print(f'Vc deve comprar o produto de R${menor} ')


main()
