# Crie uma classe Equipamento com atributos como nome, fabricante e
# ano_de_fabricacao. Crie uma classe derivada Computador, que tenha atributos adicionais
# como processador e memoria_ram. Implemente métodos para exibir as especificações
# completas do equipamento.


class Equipamento:
    def __init__(self, nome, fabricante, ano_de_fabricacao):
        self._nome = nome
        self._fabricante = fabricante
        self._ano_de_fabricacao = ano_de_fabricacao
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @property
    def ano_de_fabricacao(self):
        return self._ano_de_fabricacao
    
    def exibir_especificacoes(self):
        return (f"Nome: {self.nome}\n"
                f"Fabricante: {self.fabricante}\n"
                f"Ano de Fabricação: {self.ano_de_fabricacao}")


class Computador(Equipamento):
    def __init__(self, nome, fabricante, ano_de_fabricacao, processador, memoria_ram):
        super().__init__(nome, fabricante, ano_de_fabricacao)
        self._processador = processador
        self._memoria_ram = memoria_ram
    
    @property
    def processador(self):
        return self._processador
    
    @property
    def memoria_ram(self):
        return self._memoria_ram
    
    def exibir_especificacoes(self):
        especificacoes_basicas = super().exibir_especificacoes()
        especificacoes_completas = (f"{especificacoes_basicas}\n"
                                    f"Processador: {self.processador}\n"
                                    f"Memória RAM: {self.memoria_ram} GB")
        return especificacoes_completas


equipamento = Equipamento("SmartTV", "Samsumg", 2018)
print(equipamento.exibir_especificacoes())

print("\n---\n")

computador = Computador("Dell G15", "Dell", 2022, "Intel Core i7", 16)
print(computador.exibir_especificacoes())
