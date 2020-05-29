def main():
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media(nota1, nota2)
print('Media de Aproveitamento conceito:')
print('''
Entre 9.0 e 10.0 - A
Entre 7.5 e 9.0  - B
Entre 6.0 e 7.5  - C
Entre 4.0 e 6.0  - D
Entre 4.0 e Zero - E
''')
print('-='*20)


def media(num1, num2):
    print('-='*20)
    media_total = (num1 + num2) / 2
    if media_total <= 4:
        print(f' sua media final foi:{media_total}, E - Reprovado!')
    elif 4 <= media_total <= 6:
        print(f'sua media final foi: {media_total}, D - Reprovado!')
    elif 6 < media_total <= 7.5:
        print(f'sua media final foi: {media_total}, C -  Aprovado')
    elif 7.5 < media_total < 9.0:
        print(f'sua media final foi:{media_total}, B - Aprovado !')
    elif 9.0 <= media_total <= 10:
        print(f'sua media final foi:{media_total}, A - Aprovado !')
    else:
        print('notas invalidas, insira notas descritas acima')


main()
