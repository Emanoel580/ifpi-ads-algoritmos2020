def main():
    hora_inicio = int(input('hora inicio: '))
    minuto_inicio = int(input('minutos iniciais: '))
    hora_fim = int(input('hora final: '))
    minutos_fim = int(input('minutos finais: '))
    duracao_jogo(hora_inicio, hora_fim, minuto_inicio, minutos_fim)


def duracao_jogo(valor1, valor2, valor3, valor4):
    if valor1 == valor2 and valor3 == valor4:
        print(f'24 horas')
    horas = valor2 - valor1
    minuto = valor4 - valor3

    if valor1 <= valor2 and valor3 <= valor4:
        print('{} horas e {} minutos'.format(horas, minuto))
    elif valor1 < valor2 and valor3 > valor4:
        print('{} horas e {} minutos'.format(horas, 60 - minuto - valor3))
    elif valor1 > valor2 and valor3 > valor4:
        hora = (24 - valor1) + valor2 + 1
        minuto = (60 - valor3) + valor4
        print('{} horas e {} minutos'.format(hora, minuto))
    elif valor1 > valor2 and valor3 == valor4:
        hora = (24 - valor1) + valor2
        minuto = valor3 - valor4
        print('{} horas e {} minutos'.format(hora, minuto))
    elif valor1 > valor2 and valor3 < valor4:
        hora = (24 - valor1) + valor2
        minuto = valor4 - valor3
        print('{} horas e {} minutos'.format(hora, minuto))


main()
