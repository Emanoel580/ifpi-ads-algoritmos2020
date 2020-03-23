def main():
    tipo_combustivel = input('A - Álcool (R$ 1.90) G - Gasolina (R$ 2.50): ').upper()
    litros = float(input('Litros: '))
    desconto_combustivel(tipo_combustivel, litros)


def desconto_combustivel(tipo, litro):
    preco_alcool = 1.90
    preco_gasolina = 2.50
    if tipo == 'A':
        if litro <= 20:
            desconto = (litro * preco_alcool) * 0.03
            valor = (litro * preco_alcool) - desconto
            print('Valor a ser pago: R$ {:.2f}'.format(valor))
            print('Desconto: R$ {:.2f}'.format(desconto))
        else:
            desconto = (litro * preco_alcool) * 0.05
            valor = (litro * preco_alcool) - desconto
            print('Valor a ser pago: R$ {:.2f}'.format(valor))
            print('Desconto: R$ {:.2f}'.format(desconto))
    elif tipo == 'G':
        if litro <= 20:
            desconto = (litro * preco_gasolina) * 0.04
            valor = (litro * preco_gasolina) - desconto
            print('Valor a ser pago: R$ {:.2f}'.format(valor))
            print('Desconto: R$ {:.2f}'.format(desconto))
        else:
            desconto = (litro * preco_gasolina) * 0.06
            valor = (litro * preco_gasolina) - desconto
            print('Valor a ser pago: R$ {:.2f}'.format(valor))
            print('Desconto: R$ {:.2f}'.format(desconto))
    else:
        print('Valor inválido')


main()
