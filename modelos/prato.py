class Prato:
    cardapio = []

    def __init__(self, nome, preco, estoque=0):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        Prato.cardapio.append(self)

    @classmethod
    def listar_pratos(cls):
        print(' CARDÁPIO '.center(70, '*'))
        for i, prato in enumerate(cls.cardapio):
            print(f'{str(i+1).ljust(3)} | {prato.nome.ljust(30)} | R${str(prato.preco).ljust(10)} | Estoque: {prato.estoque}')
        print('*'*70)
