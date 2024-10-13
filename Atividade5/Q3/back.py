from datetime import datetime

class EstoqueMedicamentos:
    def __init__(self, nome, quantidade, data_validade):
        self._nome = nome
        self._quantidade = quantidade
        self._data_validade = data_validade

    @property
    def nome(self):
        return self._nome

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def data_validade(self):
        return self._data_validade

    def esta_perto_vencimento(self):
        # Converte datetime.now() para um objeto date para a comparação funcionar
        return (self._data_validade - datetime.now().date()).days <= 30

    def remover(self, quantidade):
        if self._quantidade - quantidade >= 0:
            self._quantidade -= quantidade

    def adicionar(self, quantidade):
        self._quantidade += quantidade
