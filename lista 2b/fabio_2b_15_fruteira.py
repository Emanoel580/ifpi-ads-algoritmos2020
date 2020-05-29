def main():
    morango = float(input('Morangos(KG): '))
    maca = float(input('Maçãs(KG): '))
    preco_frutas(morango, maca)


def preco_frutas(fruta_1, fruta_2):
    total_frutas = fruta_1 + fruta_2
    if total_frutas <= 5:
        preco_morango = fruta_1 * 2.50
        preco_maca = fruta_2 * 1.80
        valor_total = preco_maca + preco_morango
        print('Valor a ser pago: R$ {:.2f}'.format(valor_total))
    else:
        preco_morango = fruta_1 * 2.20
        preco_maca = fruta_2 * 1.50
        valor_total = preco_maca + preco_morango
        if total_frutas > 8 or valor_total > 25:
            desconto = valor_total * 0.1
            valor_descontado = valor_total - desconto
            print('PARABÉNS, GANHOU DESCONTO DE 10%')
            print('Valor sem desconto: R$ {:.2f}'.format(valor_total))
            print('Valor a ser pago: R$ {:.2f}'.format(valor_descontado))
        else:
            print('Valor a ser pago R$ {:.2f}'.format(valor_total))


main()