def main():
    letra = str(input('diga uma letra: '))
    sexo(letra)


def sexo(valor1):
    if valor1 == 'F':
        print('F - Feminino')
    elif valor1 == 'M':
        print('M - Masculino')
    else:
        print('Sexo invalido')


main()
