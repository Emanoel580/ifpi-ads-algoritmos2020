def main():
    turno = str(input(' qual seu turno: '))
    cumprimento(turno)


def cumprimento(valor1):
    if valor1 == "M":
        print('Bom dia !')
    elif valor1 == "V":
        print('Boa tarde !')
    else:
        print('Boa noite !')


main()
