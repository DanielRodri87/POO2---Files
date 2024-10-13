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
        Este método deve ser implementado por qualquer classe que herde de Pagamento.
        """
        pass

    @valor_transacao.setter
    @abstractmethod
    def valor_transacao(self, valor):
        """
        Define o valor da transação.
        Este método deve ser implementado por qualquer classe que herde de Pagamento.
        """
        pass

    @abstractmethod
    def processar_pagamento(self):
        """
        Processa o pagamento. A lógica de processamento de pagamento
        deverá ser definida nas classes concretas que herdem de Pagamento.
        """
        pass

    @abstractmethod
    def emitir_recibo(self):
        """
        Emite um recibo para o pagamento processado. A implementação deste
        método deve ser definida nas classes concretas que herdem de Pagamento.
        """
        pass


class PagamentoCredito(Pagamento):
    """
    Classe que representa um pagamento via cartão de crédito.
    Implementa todos os métodos abstratos da interface Pagamento.
    """

    def __init__(self, valor):
        """
        Construtor que inicializa o valor da transação.
        """
        self._valor_transacao = valor

    @property
    def valor_transacao(self):
        """
        Retorna o valor da transação.
        """
        return self._valor_transacao

    @valor_transacao.setter
    def valor_transacao(self, valor):
        """
        Define o valor da transação.
        """
        self._valor_transacao = valor

    def processar_pagamento(self):
        """
        Implementa o processamento do pagamento via cartão de crédito.
        Retorna uma mensagem indicando o valor processado.
        """
        return f"Processando pagamento de R${self.valor_transacao:.2f} via cartão de crédito."

    def emitir_recibo(self):
        """
        Emite um recibo para o pagamento realizado via cartão de crédito.
        Retorna uma mensagem com o valor e o meio de pagamento.
        """
        return f"Recibo: Pagamento de R${self.valor_transacao:.2f} recebido via cartão de crédito."


class PagamentoBoleto(Pagamento):
    """
    Classe que representa um pagamento via boleto bancário.
    Implementa todos os métodos abstratos da interface Pagamento.
    """

    def __init__(self, valor):
        """
        Construtor que inicializa o valor da transação.
        """
        self._valor_transacao = valor

    @property
    def valor_transacao(self):
        """
        Retorna o valor da transação.
        """
        return self._valor_transacao

    @valor_transacao.setter
    def valor_transacao(self, valor):
        """
        Define o valor da transação.
        """
        self._valor_transacao = valor

    def processar_pagamento(self):
        """
        Implementa o processamento do pagamento via boleto bancário.
        Retorna uma mensagem indicando o valor processado.
        """
        return f"Processando pagamento de R${self.valor_transacao:.2f} via boleto bancário."

    def emitir_recibo(self):
        """
        Emite um recibo para o pagamento realizado via boleto bancário.
        Retorna uma mensagem com o valor e o meio de pagamento.
        """
        return f"Recibo: Pagamento de R${self.valor_transacao:.2f} recebido via boleto bancário."

Pagamento.register(PagamentoCredito)
Pagamento.register(PagamentoBoleto)

pagamento_cartao = PagamentoCredito(150.75)

print(pagamento_cartao.processar_pagamento())  
print(pagamento_cartao.emitir_recibo())       

pagamento_cartao.valor_transacao = 200.00

print(pagamento_cartao.processar_pagamento()) 
print(pagamento_cartao.emitir_recibo())        
pagamento_boleto = PagamentoBoleto(350.50)

print(pagamento_boleto.processar_pagamento())  
print(pagamento_boleto.emitir_recibo())       

pagamento_boleto.valor_transacao = 400.00

print(pagamento_boleto.processar_pagamento())  
print(pagamento_boleto.emitir_recibo())        
