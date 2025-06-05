tamanho = int(input("Informe um tamanho: "))

def quadrado1(tamanho):
    for i in range(tamanho):
        print("*" * tamanho )


quadrado1(tamanho)

def quadrado2(tamanho):
    meio = tamanho // 2
    for i in range(tamanho):
        linha = ''
        for j in range(tamanho):
            if i == meio and j == meio:
                linha += ' '
            else:
                linha += "*"
        print(linha)

    
quadrado2(tamanho)

def piramide(tamanho):
    altura = tamanho // 2
    for i in range(altura + 1):
        espacos =" " * (altura-i)
        asteristicos = '*' * (2*i+1)
        print(espacos + asteristicos + espacos)
        
piramide(tamanho)
        