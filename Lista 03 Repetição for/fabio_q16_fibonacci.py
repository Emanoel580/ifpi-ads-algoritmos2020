# Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
# (0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.
n = int(input('numero: '))
anterior = 0
atual = 1


for i in range(n):
    proximo = anterior + atual
    print(anterior, end=' ')
    anterior = atual
    atual = proximo