class Jogo:
    def __init__(self, titulo, genero, avaliacao):
        self._titulo = titulo
        self._genero = genero
        self._avaliacao = avaliacao

    @property
    def titulo(self):
        return self._titulo
    @property
    def genero(self):
        return self._genero
    @property
    def avaliacao(self):
        return self._avaliacao
    
    @avaliacao.setter
    def avaliacao(self, novo):
        if (novo >= 0 and novo <= 10):
            self._avaliacao = novo

class BibliotecaJogos:
    def __init__(self):
        self._lita_objetos = []
        self._avaliacoes = []

    def cadastrar_jogos(self, input_titulo, input_genero, input_avaliacao):
        jogo = Jogo(input_titulo, input_genero, input_avaliacao)
        self._lita_objetos.append(jogo)
        self._avaliacoes.append(input_avaliacao)
    

    def listar_jogos(self, source_genero):
        for x in self._lita_objetos:
            if (x.genero == source_genero):
                return True, f"Nome: {x.titulo}\nGênero: {x.genero}\n Avaliação: {x.avaliacao}"
        
    def calcular_media_avaliacoes(self, source_genero):
        for x in self._lita_objetos:
            if (x.genero == source_genero):
                total = sum(self._avaliacoes)
                return total / len(self._lita_objetos)


