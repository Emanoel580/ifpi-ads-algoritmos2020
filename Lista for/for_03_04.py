A0 = int(input('primeiro termo: '))
Limite = int(input('ultimo termo: '))
R = int(input('razão: '))
print('=' * 20)

pg = [A0 * R ** (n - 1) for n in range(1, Limite + 1)]
print(pg)
print('Fim !')
print('=' * 20)



