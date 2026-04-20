from modelos.prato import Prato
from modelos.cliente import Cliente
from modelos.pedido import Pedido

def menu():
    pedidos = [] 

    print(' SEJA BEM-VINDO(A) '.center(30, '='))
    print('1 | Cardápio')
    print('2 | Fazer pedido')
    print('3 | Remover prato')
    print('4 | Listar pedido')
    print('5 | Fechar pedido')
    print('='*30)

    while True:
        try:
            op = int(input('Escolha a opção (0 para sair): '))
        except (ValueError, TypeError):
            print('Opção inválida!')
            continue
        
        match op:
            case 1:
                cardapio()
            case 2:
                cardapio()
                nome_cliente = input('Nome do cliente: ')
                cliente = Cliente(nome_cliente)
                pedido = fazer_pedido(cliente)
                pedidos.append(pedido)
            case 3:
                print(' REMOÇÃO DE PEDIDO '.center(50, '='))
                remover_prato(pedidos)
            case 4:
                print(' PEDIDOS '.center(50, '='))
                listar_pedido(pedidos)
            case 5:
                print(' FECHAMENTO DE CONTA '.center(50, '='))
                fechamento_pedido(pedidos)
            case 0:
                break
            case _:
                print('Opção inválida.')   

def tratamento_erro(escolha):
    while True:
        try:
            return int(input(escolha))
        except (ValueError, TypeError):
            print('Opção inválida!')
            continue

# Mostrar cardápio 
def cardapio():
    Prato.listar_pratos()
    return

# Fazer pedido 
def fazer_pedido(cliente):
    pedido = Pedido(cliente)

    while True:
        op = tratamento_erro('Número do prato (0 para finalizar): ')

        if op == 0:
            break
        
        try:
            indice = op - 1
            prato = Prato.cardapio[indice]
            pedido.adicionar_prato(prato)
        except (ValueError, TypeError):
            print('Opção inválida!')

    return pedido

# Listar pedido
def listar_pedido(pedidos):
    if not pedidos:
        print('Nenhum pedido encontrado.')
        return

    for i, pedido in enumerate(pedidos):
        print(f'{i+1} |', end=' ')
        pedido.listar_pedido()

# Remover prato
def remover_prato(pedidos):
    if not pedidos:
        print('Nenhum pedido encontrado.')
        return

    while True:
        listar_pedido(pedidos)
        op_pedido = tratamento_erro('Número do pedido (0 para finalizar): ')
            
        if op_pedido == 0:
            break

        indice_pedido = op_pedido - 1

        if indice_pedido < 0 or indice_pedido >= len(pedidos):
            print('Pedido inválido.')
            continue

        pedido = pedidos[indice_pedido]
        pedido.listar_pedido()

        if not pedido.pratos:
            print('Pedido sem pratos.')
            continue

        op_prato = tratamento_erro('Número do prato: ')

        indice_prato = op_prato - 1

        if indice_prato < 0 or indice_prato >= len(pedido.pratos):
            print('Prato inválido.')
            continue

        prato = pedido.pratos[indice_prato]
        pedido.remover_prato(prato)

def fechamento_pedido(pedidos):
    while True:
        op = tratamento_erro('Fechar pedido (0 para finalizar): ')

        if op == 0:
            break

        listar_pedido(pedidos)

        try:
            indice = op - 1
            pedido = pedidos[indice]
            pedido.fechar_pedido()
        except (ValueError, TypeError, IndexError):
            print('Opção inválida!')
        

# Pratos
p1 = Prato('Macarrão Bolonhesa', 35, estoque=10)
p2 = Prato('Parmegiana de Carne', 50, estoque=8)
p3 = Prato('Strogonoff de Frango', 40, estoque=3)
p4 = Prato('Feijoada', 55)
p5 = Prato('Moqueca de Peixe', 120)
p6 = Prato('Costela ao Molho Barbecue', 90, estoque=1)
p7 = Prato('Ceasar Salad', 35, estoque=6)
p8 = Prato('Pudim', 25, estoque=7)
p9 = Prato('Petit Gateau', 30, estoque=5)
p10 = Prato('Sorvete de Chocolate', 20, estoque=2)

# Clientes

menu()