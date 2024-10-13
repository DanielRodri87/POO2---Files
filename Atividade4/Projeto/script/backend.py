class Cliente:
    def __init__(self, nome, cpf, endereco, cep, fone):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._cep = cep
        self._fone = fone

    def get_nome(self):
        return self._nome

    def get_cpf(self):
        return self._cpf

    def get_endereco(self):
        return self._endereco

    def get_cep(self):
        return self._cep

    def get_fone(self):
        return self._fone


class Cadastro:
    def __init__(self):
        self._dict_info = {}
        self._conta_cliente = 0

    def cadastra(self, cliente):
        self._dict_info[cliente.get_cpf()] = cliente
        self._conta_cliente += 1

    def total(self):
        return True, self._conta_cliente

    def verifica(self, cliente):
        if cliente.get_cpf() in self._dict_info.keys():
            return True, "Encontrado"
        return False, "Não encontrado"

    def get_cliente_info(self, cpf):
        return self._dict_info.get(cpf, None)
