#Imprima uma tabuada escolhida pelo usuário 
#Utilize time, função

import time

numero = int(input("Tabuada do número: "))

def tabuada(numero):

    for i in range(0,11):
        print(f"{numero} x {i} = {numero * i}")
        time.sleep(1)

tabuada(numero)
