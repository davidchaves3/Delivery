from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def atualizar(self, status: str):
        pass

class Cliente(Observador):
    def __init__(self, nome: str):
        self.nome = nome

    def atualizar(self, status: str):
        print(f"Cliente {self.nome}: Status do pedido - '{status}'!")

class Entregador(Observador):
    def __init__(self, nome: str):
        self.nome = nome

    def atualizar(self, status: str):
        if status == "Pedido aguardando retirada":
            print(f"Entregador {self.nome}: Pedido aguardando retirada!")
        elif status == "Saiu para entrega":
            print(f"Entregador {self.nome}: Pedido em rota!")

class Restaurante(Observador):
    def __init__(self, nome: str):
        self.nome = nome

    def atualizar(self, status: str):
        if status == "Preparando":
            print(f"Restaurante {self.nome}: Iniciando a preparação do pedido!")