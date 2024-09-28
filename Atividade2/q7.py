# Desenvolva uma classe Produto com atributos como nome, preco e
# quantidade_estoque. Crie métodos para:
# • Adicionar produtos ao estoque.
# • Remover produtos do estoque.
# • Exibir uma lista de produtos com baixa quantidade no estoque (por exemplo,
# menos de 5 unidades).

class Produto:
    def __init__(self, nome, preco, qtd):
        self._nome = nome
        self._preco = preco
        self._qtd = qtd
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def qtd(self):
        return self._qtd
    
    @qtd.setter
    def qtd(self, valor):
        self._qtd = valor

class Sistema:
    def __init__(self):
        self._produtos = []
        
    @property
    def produtos(self):
        return self._produtos
    
    def add_estoque(self, obj_prod):
        self.produtos.append(obj_prod)
        return True, "Produto adicionado com sucesso"
    
    def remover_estoque(self, nome, qtd):
        source = 0
        for x in self.produtos:
            if x.nome == nome:
                if x.qtd >= qtd:
                    x.qtd -= qtd
                    source = 1
                    if x.qtd == 0:
                        self.produtos.remove(x)
                else:
                    return False, "Quantidade insuficiente no estoque"
        
        if source:
            return True, "Produto removido com sucesso"
        else:
            return False, "Produto não encontrado"
    
    def baixo_estoque(self):
        produtos_baixo_estoque = []
        for x in self.produtos:
            if x.qtd < 5:
                produtos_baixo_estoque.append(f"Nome: {x.nome} | Quantidade: {x.qtd}")
        
        if produtos_baixo_estoque:
            return produtos_baixo_estoque
        else:
            return "Nenhum produto com baixa quantidade no estoque"
        

p1 = Produto("Arroz", 20.5, 4)
p2 = Produto("Feijão", 10.0, 10)
p3 = Produto("Açúcar", 5.0, 3)

sistema = Sistema()
sistema.add_estoque(p1)
sistema.add_estoque(p2)
sistema.add_estoque(p3)

print(sistema.baixo_estoque())  
print(sistema.remover_estoque("Arroz", 2)[1]) 
