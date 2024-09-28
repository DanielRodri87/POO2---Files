class Estudante:
    def __init__(self, nome, nota):
        self._nome = nome
        self._nota = nota
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def nota(self):
        return self._nota


class Turma:
    def __init__(self):
        self._estudantes = []
    
    @property
    def estudantes(self):
        return self._estudantes
    
    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)
        return f"Estudante {estudante.nome} adicionado com sucesso."
    
    def remover_estudante(self, nome):
        for estudante in self.estudantes:
            if estudante.nome == nome:
                self.estudantes.remove(estudante)
                return f"Estudante {nome} removido com sucesso."
        return f"Estudante {nome} não encontrado."
    
    def calcular_media(self):
        if not self.estudantes:
            return 0
        total_notas = sum(estudante.nota for estudante in self.estudantes)
        return total_notas / len(self.estudantes)
    
    def exibir_acima_media(self):
        media = self.calcular_media()
        estudantes_acima_media = [estudante for estudante in self.estudantes if estudante.nota > media]
        
        if estudantes_acima_media:
            return [f"Nome: {estudante.nome} | Nota: {estudante.nota}" for estudante in estudantes_acima_media]
        else:
            return "Nenhum estudante com nota acima da média."

e1 = Estudante("Alice", 8.5)
e2 = Estudante("Bob", 6.0)
e3 = Estudante("Carol", 9.0)

turma = Turma()
turma.adicionar_estudante(e1)
turma.adicionar_estudante(e2)
turma.adicionar_estudante(e3)

print(f"Média da turma: {turma.calcular_media():.2f}")
print("Estudantes com nota acima da média:")
print(turma.exibir_acima_media())
