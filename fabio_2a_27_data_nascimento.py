def main():
    dia1 = int(input('dia de nascimento: '))
    mes1 = int(input('mes de nascimento: '))
    ano1 = int(input('ano de nascimento: '))
    dia2 = int(input('dia atul:'))
    mes2 = int(input('mes atual:'))
    ano2 = int(input('ano atual:'))
    idade(dia1, dia2, mes1, mes2, ano1, ano2)


def idade(valor1, valor2, valor3, valor4, valor5, valor6):
    if valor6 > valor5 and valor4 > valor3 and valor2 > valor1:
        ano = valor6 - valor5
        mes = valor4 - valor3
        dia = valor2 - valor1
        print('{} anos, {} mes(s) e {} dia(s)'.format(ano, mes, dia))
    elif valor6 > valor5 and valor4 < valor3 and valor2 > valor1:
        ano = (valor6 - valor5) - 1
        mes = valor3 - valor4
        dia = valor2 - valor1
        print('{} anos, {} mes(s) e {} dia(s)'.format(ano, mes, dia))
    elif valor6 > valor5 and valor4 < valor3 and valor1 > valor2:
        ano = (valor6 - valor5) - 1
        mes = valor3 - valor4
        dia = valor1 - valor2
        print('{} anos, {} mes (s) e {} dias'.format(ano, mes, dia))
    elif valor6 > valor5 and valor4 == valor3 and valor1 > valor2:
        ano = valor6 - valor5
        mes = valor4 - valor3
        dia = valor1 - valor2
        print('{}anos, {} mes e {} dias'.format(ano, mes, dia))
    elif valor6 > valor5 and valor4 == valor3 and valor2 > valor1:
        ano = valor6 - valor5
        mes = valor4 - valor3
        dia = valor2 - valor1
        print('{} anos, {} mes e {} dia'.format(ano, mes, dia))
    elif valor6 > valor5 and valor4 < valor3 and valor2 == valor1:
        ano = valor6 - valor5 - 1
        mes = valor3 - valor4
        dia = valor1 - valor2
        print('{} anos, {} meses e {} dias'.format(ano, mes, dia))
    elif valor6 > valor5 and valor4 == valor3 and valor2 == valor1:
        ano = valor6 - valor5
        mes = valor4 - valor3
        dia = valor2 - valor1
        print('{} anos, {} mes(s) e dia (s)'.format(ano, mes, dia))
    elif valor6 > valor5 and valor4 > valor3 and valor2 == valor1:
        ano = valor6 - valor5
        mes = valor3 - valor4
        dia = valor2 - valor1
        print('{} anos, {} mes e {} dia'.format(ano, mes, dia))

    else:
        print('0 anos')


main()
