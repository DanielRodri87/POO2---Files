#  Crie uma classe Funcionario com os atributos nome e salario. Implemente um
# método para calcular o aumento de salário com base em um percentual fornecido. Crie
# uma classe derivada Gerente, que herde de Funcionario e adicione um bônus ao salário
# no cálculo final.

class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, novo):
        self._salario = novo
    
    def aumento(self, percentual):
        if percentual > 0:
            self._salario += self._salario * (percentual / 100)
            return True, f"Novo salário de {self.nome}: R${self.salario:.2f}"
        return False, "Percentual inválido"


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def aumento(self, percentual):
        if percentual > 0:
            self._salario += self._salario * (percentual / 100) + self.bonus
            return True, f"Novo salário de {self.nome} (Gerente): R${self.salario:.2f} com bônus"
        return False, "Percentual inválido"


if __name__ == "__main__":
    funcionario = Funcionario("Daniel", 3000)
    resultado_func, mensagem_func = funcionario.aumento(10)
    print(mensagem_func)  

    gerente = Gerente("Rodrigues", 5000, 500)
    resultado_gerente, mensagem_gerente = gerente.aumento(10)
    print(mensagem_gerente)  
