import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QMessageBox
from back import BibliotecaJogos

class BibliotecaJogosApp(QWidget):
    def __init__(self):
        super().__init__()
        self.biblioteca = BibliotecaJogos()
        self.initUI()

    def initUI(self):
        # Layout principal
        self.layout = QVBoxLayout()

        # Campo para título do jogo
        self.titulo_input = QLineEdit(self)
        self.titulo_input.setPlaceholderText("Digite o título do jogo")
        self.layout.addWidget(self.titulo_input)

        # Campo para gênero do jogo
        self.genero_input = QComboBox(self)
        self.genero_input.addItems(["Ação", "Aventura", "RPG", "Esportes", "Estratégia"])
        self.layout.addWidget(self.genero_input)

        # Campo para avaliação
        self.avaliacao_input = QLineEdit(self)
        self.avaliacao_input.setPlaceholderText("Digite a avaliação do jogo (0-10)")
        self.layout.addWidget(self.avaliacao_input)

        # Botão para cadastrar jogo
        self.cadastrar_btn = QPushButton("Cadastrar Jogo", self)
        self.cadastrar_btn.clicked.connect(self.cadastrar_jogo)
        self.layout.addWidget(self.cadastrar_btn)

        # Campo para buscar jogos por gênero
        self.buscar_genero_input = QComboBox(self)
        self.buscar_genero_input.addItems(["Ação", "Aventura", "RPG", "Esportes", "Estratégia"])
        self.layout.addWidget(self.buscar_genero_input)

        # Botão para listar jogos por gênero
        self.listar_btn = QPushButton("Listar Jogos por Gênero", self)
        self.listar_btn.clicked.connect(self.listar_jogos)
        self.layout.addWidget(self.listar_btn)

        # Botão para calcular média de avaliações
        self.media_btn = QPushButton("Calcular Média de Avaliações", self)
        self.media_btn.clicked.connect(self.calcular_media_avaliacoes)
        self.layout.addWidget(self.media_btn)

        # Campo para exibir resultados
        self.resultado_label = QLabel(self)
        self.layout.addWidget(self.resultado_label)

        self.setLayout(self.layout)
        self.setWindowTitle("Biblioteca de Jogos")
        self.setGeometry(100, 100, 400, 300)
        self.show()

    def cadastrar_jogo(self):
        titulo = self.titulo_input.text()
        genero = self.genero_input.currentText()
        avaliacao = self.avaliacao_input.text()

        if titulo and avaliacao.isdigit() and 0 <= int(avaliacao) <= 10:
            self.biblioteca.cadastrar_jogos(titulo, genero, int(avaliacao))
            QMessageBox.information(self, "Sucesso", "Jogo cadastrado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "Por favor, insira dados válidos.")

    def listar_jogos(self):
        genero = self.buscar_genero_input.currentText()
        result = self.biblioteca.listar_jogos(genero)
        if result:
            self.resultado_label.setText(result[1])
        else:
            self.resultado_label.setText("Nenhum jogo encontrado para esse gênero.")

    def calcular_media_avaliacoes(self):
        genero = self.buscar_genero_input.currentText()
        media = self.biblioteca.calcular_media_avaliacoes(genero)
        if media:
            self.resultado_label.setText(f"Média de Avaliações para {genero}: {media:.2f}")
        else:
            self.resultado_label.setText("Nenhuma avaliação disponível para esse gênero.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BibliotecaJogosApp()
    sys.exit(app.exec_())
