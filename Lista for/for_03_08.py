def main():
    n = int(input('N: '))
    limite_inferior = int(input('inferior: '))
    limite_superior = int(input('superior: '))

    while limite_inferior <= limite_superior:
        if limite_inferior % n == 0:
            print(limite_inferior)
        limite_inferior =+ 1


main()



