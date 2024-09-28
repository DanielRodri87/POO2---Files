class Funcionario:
    """
    Classe base para representar um funcionário.
    
    Atributos:
        salario_base (float): O salário base do funcionário.
    """
    
    def __init__(self, salario_base):
        """
        Inicializa um funcionário com um salário base.

        Args:
            salario_base (float): O salário base do funcionário.
        """
        self._salario_base = salario_base
    
    @property
    def salario_base(self):
        """
        Retorna o salário base do funcionário.

        Returns:
            float: O salário base do funcionário.
        """
        return self._salario_base

    @salario_base.setter
    def salario_base(self, valor):
        """
        Define o salário base do funcionário.

        Args:
            valor (float): O novo salário base do funcionário.
        """
        self._salario_base = valor

    def calcular_salario(self):
        """
        Calcula o salário do funcionário.

        Este método deve ser sobrescrito pelas subclasses.
        
        Returns:
            float: O salário calculado.
        """
        return self._salario_base



class Gerente(Funcionario):
    """
    Classe que representa um Gerente, que é um tipo de funcionário.
    """
    
    def calcular_salario(self):
        """
        Calcula o salário do gerente, que recebe 20% a mais do que o salário base.

        Returns:
            float: O salário do gerente.
        """
        return self.salario_base * 1.2


class Desenvolvedor(Funcionario):
    """
    Classe que representa um Desenvolvedor, que é um tipo de funcionário.
    """
    
    def calcular_salario(self):
        """
        Calcula o salário do desenvolvedor, que recebe 10% a mais do que o salário base.

        Returns:
            float: O salário do desenvolvedor.
        """
        return self.salario_base * 1.1


funcionario = Funcionario(3000)
gerente = Gerente(5000)
desenvolvedor = Desenvolvedor(4000)

print(f"Salário base: {funcionario.calcular_salario()}")
print(f"Salário do gerente: {gerente.calcular_salario()}")
print(f"Salário do desenvolvedor: {desenvolvedor.calcular_salario()}")

