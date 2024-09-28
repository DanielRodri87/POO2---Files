class Item:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco


class Pedido:
    def __init__(self):
        self._itens = []
    
    @property
    def itens(self):
        return self._itens
    
    def adicionar_item(self, item):
        self.itens.append(item)
        return f"Item {item.nome} adicionado ao pedido."
    
    def remover_item(self, nome):
        for item in self.itens:
            if item.nome == nome:
                self.itens.remove(item)
                return f"Item {nome} removido do pedido."
        return f"Item {nome} não encontrado no pedido."
    
    def calcular_total(self):
        total = sum(item.preco for item in self.itens)
        return total
    
    def exibir_pedido(self):
        if not self.itens:
            return "O pedido está vazio."
        
        pedido_str = "\n".join([f"Item: {item.nome} | Preço: R$ {item.preco:.2f}" for item in self.itens])
        return f"Pedido:\n{pedido_str}\nTotal: R$ {self.calcular_total():.2f}"


item1 = Item("Figado", 5.0)
item2 = Item("Arroz Carreteiro", 10.0)
item3 = Item("Feijoada", 18.0)

pedido = Pedido()
pedido.adicionar_item(item1)
pedido.adicionar_item(item2)
pedido.adicionar_item(item3)

print(pedido.exibir_pedido()) 

pedido.remover_item("Arroz Carreteiro")
print(pedido.exibir_pedido()) 
