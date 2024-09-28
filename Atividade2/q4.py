class Veiculo:
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
    
    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def ano(self):
        return self._ano

    def exibir_informacoes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self._num_portas = num_portas
    
    @property
    def num_portas(self):
        return self._num_portas

    def exibir_informacoes(self):
        info_base = super().exibir_informacoes()
        return f"{info_base}, Número de portas: {self.num_portas}"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cc):
        super().__init__(marca, modelo, ano)
        self._cc = cc
    
    @property
    def cc(self):
        return self._cc

    def exibir_informacoes(self):
        info_base = super().exibir_informacoes()
        return f"{info_base}, Cilindradas: {self.cc}"


carro = Carro("Toyota", "Corolla", 2024, 4)
moto = Moto("Honda", "POP100", 2008, 99)

print(carro.exibir_informacoes())
print(moto.exibir_informacoes())
