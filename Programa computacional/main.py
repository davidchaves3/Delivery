from models.pedido import Pedido
from models.observador import Cliente, Entregador, Restaurante

def main():
    pedido = Pedido()
    cliente = Cliente("João")
    entregador = Entregador("Carlos")
    restaurante = Restaurante("Pizza Express")

    pedido.adicionar_observador(cliente)
    pedido.adicionar_observador(entregador)
    pedido.adicionar_observador(restaurante)

    while True:
        print("\n--- MENU ---")
        print("1 - Mudar status do pedido")
        print("2 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nEscolha um novo status:")
            print("1 - Recebido")
            print("2 - Preparando")
            print("3 - Pedido aguardando retirada")
            print("4 - Saiu para entrega")
            print("5 - Entregue")
            status_opcao = input("Digite o número do status: ")

            status_dict = {
                "1": "Recebido",
                "2": "Preparando",
                "3": "Pedido aguardando retirada",
                "4": "Saiu para entrega",
                "5": "Entregue"
            }

            if status_opcao in status_dict:
                pedido.mudar_status(status_dict[status_opcao])
            else:
                print("Opção inválida! Tente novamente.")
        elif opcao == "2":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()