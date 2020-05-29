def main():
    dia = int(input('dia: '))
    mes = int(input('mes: '))
    ano = int(input('ano: '))
    dia_nascimento = int(input('dia de nascimento: '))
    mes_nascimento = int(input('mes: '))
    ano_nascimento = int(input('ano nascimento: '))
    idade_pessoa(dia, mes, ano, dia_nascimento, mes_nascimento, ano_nascimento)


def idade_pessoa(dia1, mes1, ano1, dia2, mes2, ano2):
    anos = ano1 - ano2
    meses_restantes = (ano1 - ano2) - 1
    if dia1 >= dia2 and mes1 >= mes2:
        print(anos, 'anos')
    else:
        print(meses_restantes, 'anos')


main()
