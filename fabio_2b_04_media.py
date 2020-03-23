def main():
    num1 = float(input('1ª nota: '))
    num2 = float(input('2ª nota: '))
    media(num1, num2)


def media(valor1, valor2):
    media_total = (valor1 + valor2) / 2
    if media_total == 10:
        print('Aprovado com distinção')
    elif media_total < 7:
        print('reprovado !')
    else:
        print('Aprovado')




main()
