def main():
    dia = int(input('dia: '))
    mes = int(input('mes: '))
    ano = int(input('ano: '))
    data_valida(dia, mes, ano)


def data_valida(dia1, mes2, ano2):
    if dia1 <= 31:
        print('valido')
    if mes2 == 1 or mes2 == 3 or mes2 == 5 or mes2 == 7 or mes2 == 8 or mes2 == 10 or mes2 == 12:
        print('valido')
    elif mes2 == 4 or mes2 == 6 or mes2 == 9 or mes2 == 11 and dia1 <= 30:
        print('valido')
    elif ano2 % 4 == 0 and ano2 % 400 != 0 or ano2 % 400 == 0:
        print('ano bissexto')
    elif dia1 <= 29:
        print('valido')
    elif mes2 > 31:
        print('invalido')
    else:
        print('data inexistente')


main()