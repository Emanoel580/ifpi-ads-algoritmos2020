n = int(input('n° habitantes:'))
salario = float(input('salario: '))
filhos = int(input('filhos:'))

cont = 1
media_filho = 0
salario_ate_mil = 0

for cont in range(n):
    media_salario = (salario * n) / n
    media_filho = filhos / n
    if salario <=1000:
        salario_ate_mil = (salario / 1000) * n

print('media de salario:',(media_salario))
print('media de filhos:', (media_filho))
print('percetual de salario ate mil:',(salario_ate_mil))    



