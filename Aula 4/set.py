# Definir um set com 3 elementos

def definir_set():
    s = {1, 2, 3, 4}
    print(type(s))
    print(s)

# Acessar pelo Índice 

"""Não é possivel acessar pelo índice"""

# Adicionar pelo Valor 

def adicionar_valor():
    s = {1, 2, 3, 4}
    s.add(5)
    print(s)

# Adiocinar Duplicado 

"""Não é possivel adicionar duplicados com o set"""

# Remover pelo Valor 

def remover_valor():
    s = {1, 2, 3, 4}
    s.remove(2)
    print(s)

if __name__ == "__main__":
    print("Definindo um set.")
    definir_set()
    print("Adicionando valor.")
    adicionar_valor()
    print("Removendo um valor.")
    remover_valor()