def main():
    print('-=' * 20)
    horas_aula = int(input('horas de aula do professor1: '))
    custo_hora = float(input('o valor por horas do professor1:'))
    horas_aula2 = int(input('horas de aula do professor2: '))
    custo_hora2 = float(input('valor por horas do professor2: '))
    preco_hora(horas_aula, custo_hora, horas_aula2, custo_hora2)


def preco_hora(valor1, valor2, valor3, valor4):
    print('-=' * 20)
    professor1 = valor1 * valor2
    professor2 = valor3 * valor4
    maior = professor1
    if professor2 > maior:
        print('o maior salario e do professor2: R${:.2f}'.format(professor2))
    elif professor1 == professor2:
        print('O salario dos dois professores são iguais !')
    else:
        print('o maior salario e do professor1: R${:.2f}'.format(professor1))


main()