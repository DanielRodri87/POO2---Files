class Contato:
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def telefone(self):
        return self._telefone


class AgendaTelefonica:
    def __init__(self):
        self._contatos = []
    
    @property
    def contatos(self):
        return self._contatos
    
    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        return f"Contato {contato.nome} adicionado com sucesso."
    
    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                return f"Contato {nome} removido com sucesso."
        return f"Contato {nome} não encontrado."
    
    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return f"Nome: {contato.nome} | Telefone: {contato.telefone}"
        return f"Contato {nome} não encontrado."
    
    def exibir_agenda(self):
        if not self.contatos:
            return "A agenda está vazia."
        
        agenda_str = "\n".join([f"Nome: {contato.nome} | Telefone: {contato.telefone}" for contato in self.contatos])
        return f"Agenda Telefônica:\n{agenda_str}"

contato1 = Contato("Daniel", "(89) 99447-4640")
contato2 = Contato("Tanembaum", "(55) 4002-8922")

agenda = AgendaTelefonica()
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)

print(agenda.exibir_agenda())

print("\n---\n")

print(agenda.buscar_contato("Daniel"))
print(agenda.buscar_contato("Alfredo")) 

agenda.remover_contato("Daniel")
print(agenda.exibir_agenda())
