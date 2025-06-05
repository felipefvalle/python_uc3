#Imprima uma contagem regressiva com o input de partida feito Pelo usuário
#Utilize while e função

import time

def contagem(num):

    while num >= 1:
        print(num)
        time.sleep(1)
        num -= 1

numero = int(input("Digite um número: "))
contagem(numero)

