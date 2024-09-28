# Implemente uma classe Time que armazena uma lista de jogadores (objetos
# da classe Jogador). A classe Jogador deve ter atributos como nome, posição e idade. O
# time deve ter métodos para adicionar e remover jogadores, além de um método que exiba
# todos os jogadores com mais de 30 anos

class Jogador:
    def __init__(self, nome, posicao, idade):
        self._nome = nome
        self._posicao = posicao
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def posicao(self):
        return self._posicao
    
    @property
    def idade(self):
        return self._idade
    
    def info_jogador(self):
        return f"Nome: {self.nome} | Posição: {self.posicao} | Idade: {self.idade}"
    
class Time:
    def __init__(self):
        self._jogadores = []
        
    @property
    def jogadores(self):
        return self._jogadores
        
    def adicionar_jogador(self, obj_jogador):
        self.jogadores.append(obj_jogador)
        return True, "Jogador adicionado"
    
    def remover_jogador(self, nome, posicao):
        for x in self.jogadores:
            if x.nome == nome and x.posicao == posicao:
                self.jogadores.remove(x)  
                return True, "Jogador Removido"
        return False, "Jogador Não encontrado"
                
    def exibir_jogadores(self):
        for x in self.jogadores:
            print(x.info_jogador())
            
    def exibir_jogadores30(self):
        for x in self.jogadores:
            if x.idade > 30:
                print(x.info_jogador())
            
    
ingaFC = Time()

daniel = Jogador("Daniel", "Goleiro", 19)
zico = Jogador("Zico", "Meia", 90)
pele_junior = Jogador("Peleé", "Atacante", 21)
iagol = Jogador("Iagol", "Zagueiro", 31)

ingaFC.adicionar_jogador(daniel)
ingaFC.adicionar_jogador(zico)
ingaFC.adicionar_jogador(pele_junior)
ingaFC.adicionar_jogador(iagol)

print("\nJogadores\n")
ingaFC.exibir_jogadores()
print("\nJogadores > 30\n")
ingaFC.exibir_jogadores30()

print("\n\n")
ingaFC.remover_jogador("Iagol", "Zagueiro")

print("\nJogadores\n")
ingaFC.exibir_jogadores()
print("\nJogadores > 30\n")
ingaFC.exibir_jogadores30()