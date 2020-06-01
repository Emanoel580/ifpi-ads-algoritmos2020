def main():
    n = int(input('n: '))
    cont = 1
    maior = 0

    while cont <= n:
        numero = int(input('numero: '))
        if numero > maior:
            maior = numero
        cont = cont + 1
    print(f'O maior numero é: {maior}')


main()





