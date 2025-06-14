from conta import ContaCorrente

contas = {
    '123': ContaCorrente('Felipe Valle', '123', 'fel123', 100.0),
    '456': ContaCorrente('Vitor', '456', 'vic123', 2500.0)
}

# Login 

ContaCorrente.mostrar_saldo(contas['123'])
