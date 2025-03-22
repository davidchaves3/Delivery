from models.observador import Observador

class Pedido:
    def __init__(self):
        self._observadores = []
        self._status = "Recebido"

    def adicionar_observador(self, observador: Observador):
        self._observadores.append(observador)

    def remover_observador(self, observador: Observador):
        self._observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.atualizar(self._status)

    def mudar_status(self, novo_status: str):
        self._status = novo_status
        print(f"\nStatus do pedido alterado para: {self._status}")
        self.notificar_observadores()