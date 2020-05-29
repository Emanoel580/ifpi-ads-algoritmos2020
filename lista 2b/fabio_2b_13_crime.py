def main():
    questao_1 = input('Telefonou para a vítima? ').upper()
    questao_2 = input('Esteve no local do crime? ').upper()
    questao_3 = input('Mora perto da vítima? ').upper()
    questao_4 = input('Devia a vítima? ').upper()
    questao_5 = input('Já trabalhou com a vítima? ').upper()
    analise(questao_1, questao_2, questao_3, questao_4, questao_5)


def analise(a, b, c, d, e):
    contador = 0
    for i in range(1):
        if a == 'SIM' or a == 'S':
            contador = contador + 1
        if b == 'SIM' or b == 'S':
            contador = contador + 1
        if c == 'SIM' or c == 'S':
            contador = contador + 1
        if d == 'SIM' or d == 'S':
            contador = contador + 1
        if e == 'SIM' or e == 'S':
            contador = contador + 1
        if contador == 5:
            print('ASSASSINO')
        elif contador == 3 or contador == 4:
            print('CÚMPLICE')
        elif contador == 2:
            print('SUSPEITO')
        else:
            print('INOCENTE')


main()
