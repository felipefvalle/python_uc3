# Definir uma tupla com 3 elementos 

def tupla():
    tupla = (1, 'Felipe', 3, True, 5)
    print(tupla)

# Acessar pelo Índice 

def acessar_indice():
    tupla = (1, 'Felipe', 3, True, 5)
    print(tupla[1])

# Alterar um Valor pelo Índice

def alterar_valor():
    tupla = (1, 'Felipe', 3, True, 5)
    tupla[3] = "Valle"
    print(tupla)
    """ERRO - Não é possivel alterar valor em uma tupla"""

# Adicionar pelo Valor 

def adicionar():
    tupla = (1, 'Felipe', 3, True, 5)
    tupla.add(8)
    print(tupla)
    """ERRO - Não é possivel adicionar pelo valor em uma tupla"""

# Remover pelo Valor 

def remover():
    tupla = (1, 'Felipe', 3, True, 5)
    tupla.remove[2]
    print(tupla)
    """ERRO - Não é possivel remover um valor de uma tupla"""

if __name__ == "__main__":
    print("Definindo uma tupla.")
    tupla()
    print("Acessando um Índice")
    acessar_indice()
