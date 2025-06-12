""" 1 - Armazene 5 frutas nas 4 estruturas (Lista/Set/Tupla/Dict)"""

import random

# Definir uma lista vazia 

frutas = []

# Criar uma estrutura de repetição para inserir os 5 elementos

# for i in range(5):
#     valor = input(f'Informe a {i+1} fruta: ')
#     frutas.append(valor)

def gerar_dados(qtd, valormin, valormax):
    return [random.randint(valormin, valormax) for _ in range(qtd)]
frutas = gerar_dados(5, 1, 10)

# Criar uma variavel para cada estrutura e fazer a devida conversão

lista_final = list(frutas)
set_final = set(frutas)
tupla_final = tuple(frutas)
dict_final = {j: valor for j, valor in enumerate(frutas)}

# Imprimir os cinco resultados 

print(f'Lista {lista_final}')
print(f'Set {set_final}')
print(f'T {tupla_final}')
print(f'Lista {dict_final}')


# 2 - Após o teste acima, aplique o random para inserir os valores na lista






