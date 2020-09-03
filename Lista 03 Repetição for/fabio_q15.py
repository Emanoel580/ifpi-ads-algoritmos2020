# Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).
def main():
    n = int(input('N: '))

    cont = 1
    soma = 1

    for i in range(n):
        print(cont)
        soma += 1
        cont += soma


main()