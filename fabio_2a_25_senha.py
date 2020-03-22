def main():
    senha = int(input('diga a senha: '))
    seguranca(senha)


def seguranca(valor1):
    if valor1 == 1234:
        print('Bom dia. Acesso permitido !')
    else:
        print('Acesso negado, senha invalida. digite a senha correta.')


main()
