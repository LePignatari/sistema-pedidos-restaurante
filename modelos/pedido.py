class Pedido:
    def __init__(self, cliente):
        self.pratos = []
        self.cliente = cliente

    def listar_pedido(self):
        print(f'Cliente: {self.cliente.nome}')
        print('-'*50)
        for i, prato in enumerate(self.pratos):
            print(f'{i+1} |{prato.nome.ljust(25)} | R${prato.preco:.2f}')
        print('-'*50)

    def adicionar_prato(self, prato):
        if prato.estoque <= 0:
            print(f"Prato '{prato.nome}' indisponível no momento.")
            return
        self.pratos.append(prato)
        print(f'|{prato.nome}| adicionado ao seu pedido.')
        prato.estoque -= 1

    def fechar_pedido(self):
        soma = sum(prato.preco for prato in self.pratos)
        print(f'Cliente: {self.cliente.nome}')
        print(f'Total: R${soma:.2f}')
        print('-'*50)
    
    def remover_prato(self, prato):
        if prato not in self.pratos:
            print(f"Não foi possível encontrar o item '{prato.nome}' dentre os pedidos.")
            return
        
        self.pratos.remove(prato)
        prato.estoque += 1
        print(f"Prato '{prato.nome}' removido do pedido.")