from abc import ABC, abstractmethod

class Pagamento(ABC):
    """
    Interface que define os métodos para processamento de pagamento.
    """

    @property
    @abstractmethod
    def valor_transacao(self):
        """
        Retorna o valor da transação.
        """
        pass

    @valor_transacao.setter
    @abstractmethod
    def valor_transacao(self, valor):
        """
        Define o valor da transação.
        """
        pass

    @abstractmethod
    def processar_pagamento(self):
        """
        Processa o pagamento.
        """
        pass

    @abstractmethod
    def emitir_recibo(self):
        """
        Emite um recibo para o pagamento processado.
        """
        pass


class PagamentoCredito(Pagamento):
    """
    Classe que representa um pagamento via cartão de crédito.
    """

    def __init__(self, valor):
        self._valor_transacao = valor

    @property
    def valor_transacao(self):
        return self._valor_transacao

    @valor_transacao.setter
    def valor_transacao(self, valor):
        self._valor_transacao = valor

    def processar_pagamento(self):
        return f"Processando pagamento de R${self.valor_transacao:.2f} via cartão de crédito."

    def emitir_recibo(self):
        return f"Recibo: Pagamento de R${self.valor_transacao:.2f} recebido via cartão de crédito."


class PagamentoBoleto(Pagamento):
    """
    Classe que representa um pagamento via boleto bancário.
    """

    def __init__(self, valor):
        self._valor_transacao = valor

    @property
    def valor_transacao(self):
        return self._valor_transacao

    @valor_transacao.setter
    def valor_transacao(self, valor):
        self._valor_transacao = valor

    def processar_pagamento(self):
        return f"Processando pagamento de R${self.valor_transacao:.2f} via boleto bancário."

    def emitir_recibo(self):
        return f"Recibo: Pagamento de R${self.valor_transacao:.2f} recebido via boleto bancário."
