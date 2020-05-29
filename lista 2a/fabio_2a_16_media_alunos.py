def main():
    nota1 = float(input('1ª nota  aluno: '))
    nota2 = float(input('2ª nota  aluno: '))
    media(nota1, nota2)


def media(valor1, valor2,):
    media_aluno = (valor1 + valor2) / 2
    if media_aluno >= 7:
        print('Aprovado !')
    elif media_aluno < 7:
        valor3 = float(input('nota do exame: '))
        if (valor3 + media_aluno) / 2 >= 5:
            print('Aprovado !')
        else:
            print('Reprovado !')


if __name__ == '__main__':
    main()
