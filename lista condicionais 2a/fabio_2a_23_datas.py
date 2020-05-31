def main():
    dia1 = int(input('dia: '))
    mes1 = int(input('mes: '))
    ano1 = int(input('ano: '))
    dia2 = int(input('dia: '))
    mes2 = int(input('mes: '))
    ano2 = int(input('ano: '))
    data(dia1, dia2, mes1, mes2, ano1, ano2)


def data(valor1, valor2, valor3, valor4, valor5, valor6):
    if valor5 > valor6:
        print('a data mais recente é: {}/{}/{}'.format(valor1, valor3, valor5))
    elif valor5 == valor6 and valor3 > valor4 and valor1 == valor2:
        print('a data mas recente é: {}/{}/{}'.format(valor1, valor3, valor5))
    elif valor6 == valor5 and valor4 == valor3 and valor1 > valor2:
        print('A data mais recente é: {}/{}/{}'.format(valor1, valor3, valor5))
    elif valor6 == valor5 and valor4 == valor3 and valor2 == valor1:
        print('Datas iguais !')
    else:
        print('A data mais recente e: {}/{}/{}'.format(valor2, valor4, valor6))


main()








