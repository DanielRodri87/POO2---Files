class Cliente:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def email(self):
        return self._email


class Produto:
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
    def __init__(self, cliente):
        self._cliente = cliente
        self._produtos = []
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def produtos(self):
        return self._produtos
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        return f"Produto {produto.nome} adicionado ao pedido."
    
    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        return total
    
    def exibir_pedido(self):
        if not self.produtos:
            return "O pedido está vazio."
        
        produtos_str = "\n".join([f"Produto: {produto.nome} | Preço: R$ {produto.preco:.2f}" for produto in self.produtos])
        return (f"Cliente: {self.cliente.nome} | Email: {self.cliente.email}\n"
                f"Produtos:\n{produtos_str}\nTotal: R$ {self.calcular_total():.2f}")

cliente1 = Cliente("Daniel", "osmbomosm@email.com")

produto1 = Produto("Notebook", 6500.0)
produto2 = Produto("Celular", 1150.0)
produto3 = Produto("Fone", 10.0)

pedido = Pedido(cliente1)
pedido.adicionar_produto(produto1)
pedido.adicionar_produto(produto2)
pedido.adicionar_produto(produto3)

print(pedido.exibir_pedido())
