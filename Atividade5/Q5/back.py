class Item:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @property
    def quantidade(self):
        return self._quantidade

    def valor_total(self):
        return self._preco * self._quantidade


class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item_nome):
        self.itens = [item for item in self.itens if item.nome != item_nome]

    def calcular_total(self):
        return sum(item.valor_total() for item in self.itens)

    def aplicar_desconto(self, cupom):
        total = self.calcular_total()
        desconto = 0
        if cupom == "DESCONTO10":
            desconto = 0.10
        elif cupom == "DESCONTO20":
            desconto = 0.20
        return total * (1 - desconto)

    def total_com_desconto(self, cupom):
        return self.aplicar_desconto(cupom)
