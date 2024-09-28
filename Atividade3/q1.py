"""
    Classe que representa um livro.

    Atributos:
        titulo (str): O título do livro.
        autor (str): O autor do livro.
        num_pag (int): O número de páginas do livro.
"""
class Livro:
    def __init__(self, titulo, autor, num_pag):
        """
            Inicializa um objeto Livro com título, autor e número de páginas.

            Args:
                titulo (str): O título do livro.
                autor (str): O autor do livro.
                num_pag (int): O número de páginas do livro.
        """
        self._titulo = titulo
        self._autor = autor
        self._num_pag = num_pag
    
    @property
    def titulo(self):
        """
            Retorna o título do livro.

            Returns:
                str: O título do livro.
        """
        return self._titulo

    @property
    def autor(self):
        """
            Retorna o autor do livro.

            Returns:
                str: O autor do livro.
        """
        return self._autor

    @property
    def num_pag(self):
        """
            Retorna o número de páginas do livro.

            Returns:
                int: O número de páginas do livro.
        """
        return self._num_pag
    

"""
    Classe responsável pelo gerenciamento dos livros

    Args:
        titulo (dict): Livro: Quantidade de Examplates
"""
class ControleEstoque:
    """
    Classe que gerencia o estoque de livros.

    Esta classe permite adicionar, remover e consultar livros no estoque.
    O estoque é armazenado como um dicionário, onde a chave é o título do livro
    e o valor é a quantidade de exemplares disponíveis.
    """
    
    def __init__(self):
        """
        Inicializa o controle de estoque com um dicionário vazio.
        """
        self._estoque = {}
        
    def adicionar_livro(self, livro):
        """
        Adiciona um livro ao estoque. Se o livro já existir no estoque, a quantidade
        é incrementada.

        Args:
            livro (Livro): O objeto Livro a ser adicionado ao estoque.
        """
        if livro.titulo not in self._estoque:
            self._estoque[livro.titulo] = 1
        else:
            self._estoque[livro.titulo] += 1
        
    def remover_livro(self, livro):
        """
        Remove um exemplar do livro do estoque. Se o livro tiver mais de um exemplar,
        a quantidade é decrementada. Se houver apenas um exemplar, ele é removido do estoque.

        Args:
            livro (Livro): O objeto Livro a ser removido do estoque.

        Returns:
            tuple: Um par (bool, str), onde o primeiro valor indica se a remoção foi bem-sucedida
                   e o segundo valor contém uma mensagem informativa.
        """
        if livro.titulo in self._estoque:
            if self._estoque[livro.titulo] > 1:
                self._estoque[livro.titulo] -= 1
            else:
                del self._estoque[livro.titulo]
            return True, "Livro removido com sucesso"
        return False, "Livro não encontrado no estoque"
    
    def consultar_livro(self, livro):
        """
        Consulta a quantidade disponível de um livro no estoque.

        Args:
            livro (Livro): O objeto Livro a ser consultado.

        Returns:
            int: A quantidade de exemplares do livro no estoque. Retorna 0 se o livro
                 não estiver no estoque.
        """
        if livro.titulo in self._estoque:
            return self._estoque[livro.titulo]
        return 0



# Testando as classes
livro1 = Livro("Livro1", "Migue", 13)


estoque = ControleEstoque()

estoque.adicionar_livro(livro1)

estoque.adicionar_livro(livro1)  

print(f"Quantidade de '{livro1.titulo}' no estoque: {estoque.consultar_livro(livro1)}")

sucesso, msg = estoque.remover_livro(livro1)
print(msg)

print(f"Quantidade de '{livro1.titulo}' no estoque: {estoque.consultar_livro(livro1)}")

print(msg)


