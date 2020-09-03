n = int(input('Eleitores: '))

c1 = 0
c2 = 0
c3 = 0
votos_nulos = 9
votos_brancos = 0

for i in range(1, n+1):
    opção_voto = int(input("voto:" ))
    if opção_voto == 1:
        c1 +=1
    if opção_voto == 2:
        c2 +=1
    if opção_voto == 3:
        c3 += 1
    if opção_voto == 9:
        votos_nulos +=1
    if opção_voto == 0:
        voto_branco +=1

print('---contando os votos---')

if c1 > c2 and c1 > c3:
        print('vencedor:',(c1))
elif c2 > c1 and c2> c3:
        print('vencedor:',(c2))
elif c3 > c1 and c3 > c2:
        print('vencedor:', (c3))
else:
    print('Haverá 2° Turno das Eleiçoes !!')



    
    








