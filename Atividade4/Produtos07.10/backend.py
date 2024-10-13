class Produto:
    def __init__(self, nome, cod, preco, qtd_esto, des):
        self.nome = nome          
        self.cod = cod         
        self.preco = preco        
        self.qtd_esto = qtd_esto  
        self.des = des            

class CadastroProduto:
    def __init__(self):
        self._produtos = {} 

    def add_produto(self, produto):
        """
        Adiciona um produto ao cadastro.
        O código do produto deve ser único.
        """
        if produto.cod in self._produtos:
            print(f"Erro: O produto com código {produto.cod} já está cadastrado.")
        else:
            self._produtos[produto.cod] = produto

    def rmv_produto(self, cod):
        """
        Remove um produto com base no código.
        """
        if cod in self._produtos:
            del self._produtos[cod]
        else:
            print(f"Erro: Produto com código {cod} não encontrado.")

    def listar_produtos(self):
        """
        Retorna o dicionário completo de produtos cadastrados.
        """
        return self._produtos

    def buscar_produto(self, cod):
        """
        Retorna um produto com base no código.
        """
        return self._produtos.get(cod, None)
