def main():
    n = int(input('n: '))
    aux = int(n ** 0.5)
    quadrado = 0

    for i in range(0, aux, n):
        if i <= n:
            quadrado = aux ** 2
    print(f'o maior quadrado é: {quadrado}')


main()
