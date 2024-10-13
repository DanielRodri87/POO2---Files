import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget, QHBoxLayout
from back import Item, CarrinhoDeCompras

class CarrinhoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.carrinho = CarrinhoDeCompras()
        self.initUI()

    def initUI(self):
        # Layout principal
        self.layout = QVBoxLayout()

        # Campos para adicionar item
        self.nome_input = QLineEdit(self)
        self.nome_input.setPlaceholderText("Nome do Item")
        self.layout.addWidget(self.nome_input)

        self.preco_input = QLineEdit(self)
        self.preco_input.setPlaceholderText("Preço")
        self.layout.addWidget(self.preco_input)

        self.quantidade_input = QLineEdit(self)
        self.quantidade_input.setPlaceholderText("Quantidade")
        self.layout.addWidget(self.quantidade_input)

        # Botão para adicionar item
        self.adicionar_btn = QPushButton("Adicionar Item", self)
        self.adicionar_btn.clicked.connect(self.adicionar_item)
        self.layout.addWidget(self.adicionar_btn)

        # Lista de itens no carrinho
        self.lista_carrinho = QListWidget(self)
        self.layout.addWidget(self.lista_carrinho)

        # Campo para aplicar cupom
        self.cupom_input = QLineEdit(self)
        self.cupom_input.setPlaceholderText("Insira o cupom de desconto")
        self.layout.addWidget(self.cupom_input)

        # Botão para calcular o total com desconto
        self.calcular_btn = QPushButton("Calcular Total", self)
        self.calcular_btn.clicked.connect(self.calcular_total)
        self.layout.addWidget(self.calcular_btn)

        # Exibir total
        self.total_label = QLabel("Total: R$ 0.00", self)
        self.layout.addWidget(self.total_label)

        # Botão para mostrar resumo da compra
        self.resumo_btn = QPushButton("Ver Resumo Final", self)
        self.resumo_btn.clicked.connect(self.mostrar_resumo)
        self.layout.addWidget(self.resumo_btn)

        # Configurações da janela
        self.setLayout(self.layout)
        self.setWindowTitle("Simulador de Compras")
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def adicionar_item(self):
        nome = self.nome_input.text()
        preco = self.preco_input.text()
        quantidade = self.quantidade_input.text()

        if not nome or not preco or not quantidade.isdigit():
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos.")
            return

        item = Item(nome, float(preco), int(quantidade))
        self.carrinho.adicionar_item(item)
        self.atualizar_lista_carrinho()

        # Limpar campos
        self.nome_input.clear()
        self.preco_input.clear()
        self.quantidade_input.clear()

    def atualizar_lista_carrinho(self):
        self.lista_carrinho.clear()
        for item in self.carrinho.itens:
            self.lista_carrinho.addItem(f"{item.nome} - {item.quantidade}x - R$ {item.preco}")

    def calcular_total(self):
        cupom = self.cupom_input.text()
        total_com_desconto = self.carrinho.total_com_desconto(cupom)
        self.total_label.setText(f"Total: R$ {total_com_desconto:.2f}")
        
        # Notificar se o total exceder um valor
        if total_com_desconto > 100:
            QMessageBox.information(self, "Desconto Aplicado", "Você recebeu um desconto por exceder R$100!")

    def mostrar_resumo(self):
        total = self.carrinho.calcular_total()
        QMessageBox.information(self, "Resumo da Compra", f"Total final: R$ {total:.2f}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CarrinhoApp()
    sys.exit(app.exec_())
