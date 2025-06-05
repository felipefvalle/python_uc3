#imprimir os numeros a partir de um input do usuario
#ate um limite definido, tambem pelo usuario
#utilize funcao definindo parametros

inicio = int(input("Informe o valor inicial: "))
final = int(input("Informe o valor final: "))

def imprimir(inicio,final):

    for numeros in range(inicio, final +1):
        print(f"{numeros}")

imprimir(inicio, final)