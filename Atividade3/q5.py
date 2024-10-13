# Implemente uma classe base Veiculo com o método calcular_ipva e utilize @property
# para acessar o valor do veículo. As subclasses Carro, Moto e Caminhao devem
# sobrescrever o método calcular_ipva. Além disso, implemente uma classe
# SistemaImpostos que calcule o IPVA de diferentes tipos de veículos, garantindo que o
# sistema seja aberto para extensão, mas fechado para modificação.


from abc import ABC, abstractmethod

class Veiculo(ABC):
    """
    Classe base que representa um veículo com valor de mercado.
    """

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        """
        Propriedade que retorna o valor do veículo.
        """
        return self._valor

    @valor.setter
    def valor(self, valor):
        """
        Propriedade para definir o valor do veículo.
        """
        self._valor = valor

    @abstractmethod
    def calcular_ipva(self):
        """
        Método abstrato para calcular o IPVA do veículo.
        Deve ser implementado pelas subclasses.
        """
        pass

class Carro(Veiculo):
    """
    Classe que representa um carro e sobrescreve o método calcular_ipva.
    O IPVA do carro é 4% do valor do veículo.
    """
    def calcular_ipva(self):
        return self.valor * 0.04 

class Moto(Veiculo):
    """
    Classe que representa uma moto e sobrescreve o método calcular_ipva.
    O IPVA da moto é 2% do valor do veículo.
    """
    def calcular_ipva(self):
        return self.valor * 0.02  

class Caminhao(Veiculo):
    """
    Classe que representa um caminhão e sobrescreve o método calcular_ipva.
    O IPVA do caminhão é 1.5% do valor do veículo.
    """
    def calcular_ipva(self):
        return self.valor * 0.015  

class SistemaImpostos:
    """
    Classe que utiliza o Princípio Aberto-Fechado (OCP) para calcular o IPVA
    de diferentes tipos de veículos sem precisar modificar o código existente.
    """
    def calcular_ipva_veiculo(self, veiculo: Veiculo):
        """
        Calcula o IPVA de um veículo usando o método calcular_ipva.
        """
        return veiculo.calcular_ipva()


carro = Carro(50000) 
moto = Moto(15000)   
caminhao = Caminhao(200000) 

sistema_impostos = SistemaImpostos()

print(f"IPVA do carro: R${sistema_impostos.calcular_ipva_veiculo(carro):.2f}")  
print(f"IPVA da moto: R${sistema_impostos.calcular_ipva_veiculo(moto):.2f}")  
print(f"IPVA do caminhão: R${sistema_impostos.calcular_ipva_veiculo(caminhao):.2f}") 

