def main():
    num = int(input('1° lado: '))
    num_2 = int(input('2° lado: '))
    num_3 = int(input('3°lado: '))
    forma_triangulo(num, num_2, num_3)


print('-=-=-=-=-= Analisando triangulos -=-=-=-=-=')


def forma_triangulo(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        print('formam triangulo')
        if a == b and b == c:
            print('equilatero !')
        elif a != b != c != a:
            print('Escaleno !')
        elif a == b or b == c or a == b:
            print('isoceles !')
    if a == 0 or b == 0 or c == 0:
        print('nao pode conter zero')
    elif a >= b + c or b >= c + a or c >= a + b:
        print('Não forma triangulo')


main()
