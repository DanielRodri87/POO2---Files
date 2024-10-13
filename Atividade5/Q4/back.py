class Aula:
    def __init__(self, titulo, nivel_dificuldade):
        self._titulo = titulo
        self._nivel_dificuldade = nivel_dificuldade
        self._concluida = False

    @property
    def titulo(self):
        return self._titulo

    @property
    def nivel_dificuldade(self):
        return self._nivel_dificuldade

    def concluir(self):
        self._concluida = True

    def esta_concluida(self):
        return self._concluida

class AulaDeIngles(Aula):
    def __init__(self, titulo, nivel_dificuldade):
        super().__init__(titulo, nivel_dificuldade)

    def exibir_palavras_chave(self):
        return ["hello", "world", "language", "learning", "study"]

class AulaDeEspanhol(Aula):
    def __init__(self, titulo, nivel_dificuldade):
        super().__init__(titulo, nivel_dificuldade)

    def exibir_palavras_chave(self):
        return ["hola", "mundo", "idioma", "aprendizaje", "estudio"]
