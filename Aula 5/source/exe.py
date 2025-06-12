# Funções - Manipulação de arquivos 

# Criar uma função que cria e adiciona um texto no arquivo

def criar_arquivo(nome_arquivo: str, conteudo: str):
    """Criar um arquivo com o nome e conteudo fornecidos."""
    with open(nome_arquivo, 'w') as arquivo: 
        arquivo.write(conteudo)
        print('Arquivo criado com sucesso.')

nome = input('Digite o nome do arquivo: ')
criar_arquivo(f'./Aula 5/arquivos/{nome}.txt', 'Este é um exemplo de arquivo criado com Python.')

# Ler o arquivo

def ler_arquivo(nome_arquivo: str) -> str:
    """Lê um arquivo"""
    with open(nome_arquivo) as arquivo:
        return arquivo.read()

nome = input('Digite o nome do arquivo: ')
print(ler_arquivo(f'./Aula 5/arquivos/{nome}.txt'))

# Adicionar conteúdo

def adicionar_conteudo(nome_arquivo: str, conteudo: str):
    """Adicionar um conteúdo."""
    with open(nome_arquivo, 'a') as arquivo: 
        arquivo.write('\n' + conteudo)
        print('Conteúdo adicionado com sucesso.')

nome = input('Digite o nome do arquivo: ')
conteudo = input('Adicione um conteúdo: ')
adicionar_conteudo(f'./Aula 5/arquivos/{nome}.txt', conteudo)

# Contar quantas linhas preenchidas possui no arquivo.

def contar_linhas(nome_arquivo: str) -> int:
    """Retorna quantas linhas tem no arquivo."""
    with open(nome_arquivo, 'r') as arquivo: 
        return len(arquivo.readlines())

nome = input('Digite o nome do arquivo: ')
print(contar_linhas(f'./Aula 5/arquivos/{nome}.txt'))

# Remover arquivo

import os

def remover_arquivo(nome_arquivo: str):
    """Remover o arquivo"""
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print('Arquivo removido com sucesso.')
    else:
        print('Arquivo não encontrado.')

nome = input('Digite o nome do arquivo que deseja remover: ')
remover_arquivo(f'./Aula 5/arquivos/{nome}.txt')

# Verificar se uma palavra existe no conteúdo.

def verificar_palavra(nome_arquivo: str, palavra: str) -> bool:
    """Vericica se a palavra existe dentro do arquivo."""
    with open(nome_arquivo, 'r') as arquivo: 
        return palavra in arquivo.read()

nome = input('Digite o nome do arquivo: ')
palavra = input('Digite uma palavra: ')
print(verificar_palavra(f'./Aula 5/arquivos/{nome}.txt', palavra))

# Criar um arquivo com 3 linhas contendo um número em cada linha 
# Criar uma função que soma os números desse arquivo

# Criando arquivo com os números

def criar_arquivo(nome_arquivo: str, conteudo: str):
    """Criar um arquivo com os números fornecidos."""
    with open(nome_arquivo, 'w') as arquivo: 
        arquivo.write(conteudo)
        print('Arquivo criado com sucesso.')

nome = input('Digite o nome do arquivo: ')
criar_arquivo(f'./Aula 5/arquivos/{nome}.txt', '1\n2\n3')

# Criando uma função para somar os números do arquivo.

def soma_conteudo(nome_arquivo: str) -> int:
    """Retorna a soma dos numeros de dentro do arquivo."""
    with open(nome_arquivo, 'r') as arquivo: 
        return sum(int(linha.strip()) for linha in arquivo)

nome = input('Digite o nome do arquivo: ')
print(soma_conteudo(f'./Aula 5/arquivos/{nome}.txt'))

# Atualizar uma linha especifica do arquivo

def atualizar_linha(nome_arquivo: str, novo_conteudo: int, linha_alvo: int):
    """Atualiza uma linha especifica dentro do arquivo."""
    with open(nome_arquivo, 'r') as arquivo: 
        linhas = arquivo.readlines()
        if 0 <= linha_alvo < len(linhas):
            linhas[linha_alvo] = novo_conteudo + '\n'

    with open(nome_arquivo, 'w') as arq:
        arq.writelines(linhas)


nome = input('Digite o nome do arquivo: ')
conteudo = input('Digite o conteúdo do arquivo: ')
linha = int(input('Digite a linha do arquivo: '))
print(atualizar_linha(f'./Aula 5/arquivos/{nome}.txt', conteudo, linha))        