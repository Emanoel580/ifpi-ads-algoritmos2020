def main():
    letra = str(input("Digite uma letra: "))
    vogal_consoante(letra)


def vogal_consoante(num):
    if num == "a" or num == "e" or num == "i" or num == "o" or num == "u":
        print('vogal !')
    else:
        print('consoante !')


main()


