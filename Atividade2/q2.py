# Implemente uma classe ContaCorrente com métodos para depositar, sacar e
# verificar o saldo. Adicione um atributo limite que permita o saque de valores maiores que
# o saldo, até um valor negativo máximo. Implemente também um método que permita
# alterar o limite da conta.

class ContaCorrente:
    def __init__(self, saldo, limite, id_conta):
        self._saldo = saldo
        self._limite = limite * -1
        self._id_conta = id_conta
        
    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite
    
    @property
    def id_conta(self):
        return self._id_conta
    
    @saldo.setter
    def saldo(self, novo):
        self._saldo = novo
    
    @limite.setter
    def limite(self, novo):
        self._limite = novo
    
    def depositar(self, id_conta_source, valor):
        if id_conta_source == self.id_conta:
            self.saldo += valor
            return True, "Deposito Realizado"
        return False, "Deposito não realizado"
            
    def sacar(self, id_conta_source, valor):
        if self._id_conta == id_conta_source:
            if self.saldo - valor >= self.limite:
                self.saldo -= valor
                return True, "Saque Realizado"
            return False, "Saque não realizado"
                
    def editar_limite(self, novo_limite):
        self.limite = novo_limite * -1
        return True, "Limite Atualizado"
    
    def verificar_saldo(self):
        print(self.saldo)
        

conta = ContaCorrente(1500, 2000, 123)
conta2 = ContaCorrente(200, 1000, 124)

conta.verificar_saldo()
saida = conta.sacar(123, 3500)
print(saida[1])
conta.verificar_saldo()


saida = conta.depositar(123, 4000)
conta.verificar_saldo()


print(saida[1])