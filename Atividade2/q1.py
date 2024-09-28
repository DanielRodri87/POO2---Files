class Livro:
    def __init__(self, titulo, autor, preco):
        self._titulo = titulo
        self._autor = autor
        self._preco = preco

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def preco(self):
        return self._preco

    @titulo.setter
    def titulo(self, novo):
        self._titulo = novo

    @autor.setter
    def autor(self, novo):
        self._autor = novo

    @preco.setter
    def preco(self, novo):
        self._preco = novo

    def exibir(self):
        print(f"Titulo: {self.titulo} | Autor: {self.autor} | Preço: {self.preco}")

class Biblioteca:
    def __init__(self):
        self.lista = [
            Livro('l1', 'autor1', 123),
            Livro('l2', 'autor2', 432),
            Livro('l3', 'autor3', 765),
            Livro('l4', 'autor4', 12)
        ]

    def exibir(self):
        for livro in self.lista:
            livro.exibir()

    def desconto(self, titulo, desconto):
        for livro in self.lista:
            if livro.titulo == titulo:
                livro.preco = livro.preco - desconto
                print(f"Desconto aplicado! Novo preço do livro '{titulo}': {livro.preco}")
    
    def exibir_filtro(self, preco_min):
        for livro in self.lista:
            if livro.preco >= preco_min:
                livro.exibir()

biblioteca = Biblioteca()
print("Exibindo informações de todos os livros:")
biblioteca.exibir()

print("\nAplicando desconto no livro 'l2':")
biblioteca.desconto('l2', 50)

print("\nExibindo livros com preço maior ou igual a 100:")
biblioteca.exibir_filtro(100)
