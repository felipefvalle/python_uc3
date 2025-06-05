
menu = ' Menu \n 1 - Carrinho de compras. \n 3 - Cadastro. \n 4 - Sair. '
def contador_menu():
    contador = 0
    while True:
        print(menu)
        escolha = int(input("Informe um valor: "))
        if escolha == 4:
            print(f"Saindo... Você interagiu {contador} vezes.")
            break
        else:
            contador +=1
contador_menu()
        