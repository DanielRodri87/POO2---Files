from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from backend import Produto, CadastroProduto  # Importa as classes do backend

app = QApplication([])
cadastro = CadastroProduto()  # Instância do cadastro

class TelaCadastro:
    def __init__(self):
        # Configurando o layout e os elementos da tela
        self.window = QWidget()
        self.window.setWindowTitle("Tela de Cadastro")
        self.window.setGeometry(100, 100, 300, 200)

        # Criando os widgets de entrada
        self.label_nome = QLabel('Nome:')
        self.input_nome = QLineEdit()

        self.label_cod = QLabel('Código:')
        self.input_cod = QLineEdit()

        self.label_preco = QLabel('Preço:')
        self.input_preco = QLineEdit()

        self.label_qtd_esto = QLabel('Quantidade em Estoque:')
        self.input_qtd_esto = QLineEdit()

        self.label_des = QLabel('Descrição:')
        self.input_des = QLineEdit()

        # Botão de salvar
        self.botao_salvar = QPushButton('Salvar Produto')
        self.botao_salvar.clicked.connect(self.salvar_dados)  # Conectando o botão à função salvar

        # Layout vertical para organizar os widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label_nome)
        layout.addWidget(self.input_nome)
        layout.addWidget(self.label_cod)
        layout.addWidget(self.input_cod)
        layout.addWidget(self.label_preco)
        layout.addWidget(self.input_preco)
        layout.addWidget(self.label_qtd_esto)
        layout.addWidget(self.input_qtd_esto)
        layout.addWidget(self.label_des)
        layout.addWidget(self.input_des)
        layout.addWidget(self.botao_salvar)
        self.window.setLayout(layout)

    def salvar_dados(self):
        nome = self.input_nome.text()
        cod = self.input_cod.text()
        preco = self.input_preco.text()
        qtd_esto = self.input_qtd_esto.text()
        des = self.input_des.text()

        produto = Produto(nome, cod, preco, qtd_esto, des)
        cadastro.add_produto(produto)

        QMessageBox.information(self.window, 'Sucesso', 'Produto cadastrado com sucesso!')

class TelaRemocao:
    def __init__(self):
        # Configurando o layout e os elementos da tela
        self.window = QWidget()
        self.window.setWindowTitle("Tela de Remoção")
        self.window.setGeometry(100, 100, 300, 200)

        # Criando os widgets de entrada
        self.label_cod = QLabel('Código:')
        self.input_cod = QLineEdit()

        # Botão de remover
        self.botao_remover = QPushButton('Remover Produto')
        self.botao_remover.clicked.connect(self.remover_dados)  # Conectando o botão à função remover

        # Layout vertical para organizar os widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label_cod)
        layout.addWidget(self.input_cod)
        layout.addWidget(self.botao_remover)
        self.window.setLayout(layout)

    def remover_dados(self):
        cod = self.input_cod.text()
        cadastro.rmv_produto(cod)

        QMessageBox.information(self.window, 'Sucesso', 'Produto removido com sucesso!')

class TelaBusca:
    def __init__(self):
        # Configurando o layout e os elementos da tela
        self.window = QWidget()
        self.window.setWindowTitle("Tela de Busca")
        self.window.setGeometry(100, 100, 300, 200)

        # Criando os widgets de entrada
        self.label_cod = QLabel('Código:')
        self.input_cod = QLineEdit()

        # Botão de buscar
        self.botao_buscar = QPushButton('Buscar Produto')
        self.botao_buscar.clicked.connect(self.buscar_dados)  # Conectando o botão à função buscar

        # Layout vertical para organizar os widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label_cod)
        layout.addWidget(self.input_cod)
        layout.addWidget(self.botao_buscar)
        self.window.setLayout(layout)

    def buscar_dados(self):
        cod = self.input_cod.text()
        produto = cadastro.listar_produtos().get(cod)

        if produto:
            QMessageBox.information(self.window, 'Sucesso', f'Produto encontrado!\nNome: {produto.nome}\nPreço: {produto.preco}\nQuantidade em estoque: {produto.qtd_esto}\nDescrição: {produto.des}')
        else:
            QMessageBox.information(self.window, 'Erro', 'Produto não encontrado!')

class TelaLista:
    def __init__(self):
        # Configurando o layout e os elementos da tela
        self.window = QWidget()
        self.window.setWindowTitle("Tela de Lista")
        self.window.setGeometry(100, 100, 300, 200)

    def listar_dados(self):
        produtos = cadastro.listar_produtos()
        lista = ''
        for cod, produto in produtos.items():
            lista += f'Código: {cod}\nNome: {produto.nome}\nPreço: {produto.preco}\nQuantidade em estoque: {produto.qtd_esto}\nDescrição: {produto.des}\n\n'

        QMessageBox.information(self.window, 'Produtos', lista)

class TelaInicial:
    def __init__(self):
        # Configurando o layout e os elementos da tela
        self.window = QWidget()
        self.window.setWindowTitle("Tela Inicial")
        self.window.setGeometry(100, 100, 300, 200)

        # Criando os botões das telas de cadastro, remoção, buscar e listar
        self.botao_cadastro = QPushButton('Cadastro de Produto')
        self.botao_cadastro.clicked.connect(self.abrir_tela_cadastro)

        self.botao_remocao = QPushButton('Remoção de Produto')
        self.botao_remocao.clicked.connect(self.abrir_tela_remocao)

        self.botao_busca = QPushButton('Busca de Produto')
        self.botao_busca.clicked.connect(self.abrir_tela_busca)

        self.botao_lista = QPushButton('Lista de Produtos')
        self.botao_lista.clicked.connect(self.abrir_tela_lista)

        # Layout vertical para organizar os widgets
        layout = QVBoxLayout()
        layout.addWidget(self.botao_cadastro)
        layout.addWidget(self.botao_remocao)
        layout.addWidget(self.botao_busca)
        layout.addWidget(self.botao_lista)
        self.window.setLayout(layout)

    def abrir_tela_cadastro(self):
        self.tela_cadastro = TelaCadastro()
        self.tela_cadastro.window.show()

    def abrir_tela_remocao(self):
        self.tela_remocao = TelaRemocao()
        self.tela_remocao.window.show()

    def abrir_tela_busca(self):
        self.tela_busca = TelaBusca()
        self.tela_busca.window.show()

    def abrir_tela_lista(self):
        self.tela_lista = TelaLista().listar_dados()

# Inicializando a tela inicial
tela_inicial = TelaInicial()
tela_inicial.window.show()

# Executando a aplicação
app.exec_()
