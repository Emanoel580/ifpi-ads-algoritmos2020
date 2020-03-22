def main():
    num = int(input('1° angulo: '))
    num_2 = int(input('2° angulo: '))
    num_3 = int(input('3° angulo: '))
    forma_triangulo(num, num_2, num_3)


def forma_triangulo(a, b, c):
    if a + b + c == 180:
        soma = a + b + c
        print('formam um triangulo !')
        if a < 90 and b < 90 and c < 90 and soma == 180:
            print('triangulo acutangulo')
        elif a == 90 or b == 90 or c == 90 and soma == 180:
            print('retangulo')
        elif a > 90 or b > 90 or c > 90 and soma == 180:
            print('obsutangulo!')
    else:
        print('não formam triangulo!')


print('-=-=-=-=-= Analisando triangulos -=-=-=-=-=')

main()
print('-=-=-=-=-= Analisando triangulos -=-=-=-=-=')

