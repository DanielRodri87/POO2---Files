# Crie uma classe Pessoa com os atributos nome e idade. Implemente um
# método para verificar se a pessoa é maior de idade. Crie uma lista de objetos Pessoa e use
# um método que filtre e retorne apenas as pessoas maiores de idade.

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade
    
class Gerencia_Pessoas:
    def __init__(self):
        self._pessoas = []
        self._adultos = []
        
    @property
    def pessoas(self):
        return self._pessoas
    
    @property
    def adultos(self):
        return self._adultos
    
        
    def adicionar_pessoa(self, obj_pessoa):
        self.pessoas.append(obj_pessoa)
        return True, "Pessoa Adicionada"
    
    def add_adultos(self):
        for x in self.pessoas:
            if x.idade >= 18:
                self.adultos.append(x)
                
    def exibir(self):
        for x in self.adultos:
            print(f"Nome: {x.nome} | Idade: {x.idade}")
            
system = Gerencia_Pessoas()

daniel = Pessoa("Daniel", 19)
zico = Pessoa("Zico", 10)
pele_junior = Pessoa("Peleé", 11)
iagol = Pessoa("Iagol", 31)

system.adicionar_pessoa(daniel)
system.adicionar_pessoa(zico)
system.adicionar_pessoa(pele_junior)
system.adicionar_pessoa(iagol)

system.add_adultos()

system.exibir()