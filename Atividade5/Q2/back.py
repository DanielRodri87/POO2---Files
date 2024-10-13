class Bicicleta:
    def __init__(self, modelo, tarifa, alugada):
        self._modelo = modelo
        self._tarifa = tarifa
        self._alugada = alugada
    
    @property
    def modelo(self):
        return self._modelo
    
    @property
    def tarifa(self):
        return self._tarifa
    
    @property
    def alugada(self):
        return self._alugada
    
    @alugada.setter
    def alugada(self, novo):
        if novo in [0, 1]:  # Deve ser 0 (livre) ou 1 (ocupada)
            self._alugada = novo
    
    def calcular_tarifa(self, quant_horas):
        return self._tarifa * quant_horas
