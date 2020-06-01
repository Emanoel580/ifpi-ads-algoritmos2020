def numeros_primo():
    n = int(input("numero: "))

    for n in range(1, n + 1):
        if n % 2 == 0:
            print(n)


numeros_primo()
