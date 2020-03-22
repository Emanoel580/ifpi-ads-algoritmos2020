def main():
    num1 = int(input('1° numero: '))
    num2 = int(input('2° numero: '))
    num3 = int(input('3° numero: '))
    num4 = int(input('4° numero: '))
    num5 = int(input('5° numero: '))
    maior(num1, num2, num3, num4, num5)
    menor(num1, num2, num3, num4, num5)


def maior(a, b, c, d, e):
   maior = a
   if b > a:
       maior = b
   if c > maior:
       maior = c
   if d > maior:
       maior = d
   if e > maior:
       maior = e
   print('o maior numero é: {}'.format(maior))


def menor(a, b, c, d, e):
   menor = a
   if b < a:
       menor = b
   if c < menor:
       menor = c
   if d < menor:
       menor = d
   if e < menor:
       menor = e
   print('o menor numero é: {}'.format(menor))


main()







