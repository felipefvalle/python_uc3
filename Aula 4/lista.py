#Definir uma lista 

def lista():
    minha_lista = [1, 2, 3]
    print(minha_lista)

#Acessar por índice

def acessar_indice():
    minha_lista = [1, 2, 3]
    print(minha_lista[0])

#Alterar por índice

def alterar_indice():
    minha_lista = [1, 2, 3]
    minha_lista[1] = 5
    print(minha_lista)

# Adicionar

def adicinar():
    minha_lista = [1, 2, 3]
    minha_lista.append(4)
    print(minha_lista)

# Adicionar por Índice

def adicionar_por_indice():
    minha_lista = [1, 2, 3]
    minha_lista.insert(0, 7)
    print(minha_lista)

# Remover por Valor 

def remover_por_valor():
    minha_lista = [1, 2, 3]
    minha_lista.remove(3)
    print(minha_lista)


# Remover por Índice

def remover_por_indice():
    minha_lista =[1, 2, 3]
    minha_lista.pop(1)
    print(minha_lista)

if __name__ == "__main__":
    print("Definindo uma lista.")
    lista()
    print("Acessando um Índice")
    acessar_indice()
    print("Alterando um Índice.")
    alterar_indice()
    print("Adicionando um Índice.")
    adicinar()
    print("Adicionando por um Índice.")
    adicionar_por_indice()
    print("Removendo Valor.")
    remover_por_valor()
    print("Removendo Índice.")
    remover_por_indice()