def pa():
    A0 = int(input('primeiro termo: '))
    Limite = int(input('ultimo termo: '))
    R = int(input('razão: '))
    print('='*20)

    for c in range(A0, Limite + 1, R):
        print(c)
    print('Fim !')
    print('=' * 20)


pa()
