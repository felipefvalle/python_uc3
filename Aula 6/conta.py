class ContaCorrente:
    def __init__(self, nome_cliente, num_conta, senha, saldo = 0.0) :
        self.nome_cliente = nome_cliente
        self.num_conta = num_conta
        # self.agencia = agencia
        self.saldo = saldo
        self.senha = senha
        # self.cheque_especial = cheque_especial
        # self.cartao_credito = cartao_credito
        # self.financiamento = financiamento
        
    def mostrar_saldo(self):
        print(f'O saldo de {self.nome_cliente} é {self.saldo:.2f}')

    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print(f'Deposito realizado com sucesso.\nSeu saldo atual é {self.saldo:.2f}')
        else:
            print('Erro - Não é possivel depositar valores negativos.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque realizado com sucesso.\nSeu saldo atual é {self.saldo:.2}')
        else:
            print('Saldo insuficiente.')
    
    def tranferir(self, valor, destinatario):
        if self.num_conta != destinatario.num_conta:
            ContaCorrente.sacar(self, valor)
            ContaCorrente.depositar(destinatario,valor)
        else:
            print('Não foi possivel realizar a transferência')

