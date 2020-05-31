def main():
    salario = float(input('diga o salario: '))
    reajuste(salario)


def reajuste(valor1):
    if valor1 > 1500:
        percentual = 5
        valor_aumento = 5 / 100 * valor1
        novo_sal = valor1 + valor_aumento
    elif valor1 > 700 and valor1 <= 1500:
        percentual = 10
        valor_aumento = 10 / 100 * valor1
        novo_sal = valor1 + valor_aumento
    elif valor1 > 280 and valor1 < 700:
        percentual = 15
        valor_aumento = 15 / 100 * valor1
        novo_sal = valor1 + valor_aumento
    else:
        percentual = 20
        valor_aumento = 20 / 100 * valor1
        novo_sal = valor1 + valor_aumento
    print(
        f'O salario antes do reajuste: R${valor1},o percentual de aumento foi de: {percentual}%, o valor do aumento'
        f'foi '
        f'de: R${valor_aumento}, novo salario: R${novo_sal}')


main()
