import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QMessageBox, QComboBox
from back import AulaDeIngles, AulaDeEspanhol

class AulaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.aulas_concluidas = []
        self.initUI()

    def initUI(self):
        # Layout principal
        self.layout = QVBoxLayout()

        # Título
        self.titulo = QLabel("Escolha uma aula de idioma:", self)
        self.layout.addWidget(self.titulo)

        # Dropdown para selecionar aula
        self.aula_combo = QComboBox(self)
        self.aula_combo.addItem("Aula de Inglês - Nível Básico")
        self.aula_combo.addItem("Aula de Espanhol - Nível Intermediário")
        self.layout.addWidget(self.aula_combo)

        # Botão para exibir palavras-chave
        self.btn_mostrar_palavras = QPushButton("Mostrar Palavras", self)
        self.btn_mostrar_palavras.clicked.connect(self.mostrar_palavras_chave)
        self.layout.addWidget(self.btn_mostrar_palavras)

        # Lista para exibir palavras-chave
        self.lista_palavras = QListWidget(self)
        self.layout.addWidget(self.lista_palavras)

        # Botão para concluir aula
        self.btn_concluir_aula = QPushButton("Concluir Aula", self)
        self.btn_concluir_aula.clicked.connect(self.concluir_aula)
        self.layout.addWidget(self.btn_concluir_aula)

        # Configurações da janela
        self.setLayout(self.layout)
        self.setWindowTitle("App de Aprendizado de Idiomas")
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def mostrar_palavras_chave(self):
        self.lista_palavras.clear()
        aula_selecionada = self.aula_combo.currentText()

        # Determina a aula selecionada
        if "Inglês" in aula_selecionada:
            aula = AulaDeIngles("Inglês - Básico", "Básico")
        else:
            aula = AulaDeEspanhol("Espanhol - Intermediário", "Intermediário")

        # Exibe as palavras-chave da aula
        palavras = aula.exibir_palavras_chave()
        for palavra in palavras:
            self.lista_palavras.addItem(palavra)

    def concluir_aula(self):
        aula_selecionada = self.aula_combo.currentText()

        # Verifica qual aula foi selecionada
        if "Inglês" in aula_selecionada:
            aula = AulaDeIngles("Inglês - Básico", "Básico")
        else:
            aula = AulaDeEspanhol("Espanhol - Intermediário", "Intermediário")

        aula.concluir()
        if aula.esta_concluida():
            self.aulas_concluidas.append(aula.titulo)
            QMessageBox.information(self, "Parabéns!", f"Aula de {aula.titulo} concluída!")

        # Exibe uma mensagem se todas as aulas foram concluídas
        if len(self.aulas_concluidas) >= 2:
            QMessageBox.information(self, "Todas as aulas concluídas", "Parabéns! Você concluiu todas as aulas disponíveis!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AulaApp()
    sys.exit(app.exec_())
