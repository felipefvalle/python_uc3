palavra = input("Digite uma palavra: ")

def verifica_palindromo(palavra):

    if palavra == palavra[::-1]:
        return True
    else:
        return False

print(verifica_palindromo(palavra))

