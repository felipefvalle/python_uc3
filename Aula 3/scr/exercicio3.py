#Some os valores do intervalo definido pelo usuário
#Utilize função e range 

inicial = int(input("Informe o valor inicial: "))
final = int(input("Informe o valor final: "))

def soma_valores(inicial, final):
    print(sum(range(inicial, final)))

soma_valores(inicial, final)

