import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QMessageBox, QLineEdit, QDateEdit, QHBoxLayout
from PyQt5.QtCore import QDate
from datetime import datetime
from back import EstoqueMedicamentos

class EstoqueApp(QWidget):
    def __init__(self):
        super().__init__()
        self.medicamentos = []
        self.initUI()

    def initUI(self):
        # Layout principal
        self.layout = QVBoxLayout()

        # Campo para adicionar medicamento
        self.nome_input = QLineEdit(self)
        self.nome_input.setPlaceholderText("Nome do Medicamento")
        self.layout.addWidget(self.nome_input)

        self.quantidade_input = QLineEdit(self)
        self.quantidade_input.setPlaceholderText("Quantidade")
        self.layout.addWidget(self.quantidade_input)

        self.data_validade_input = QDateEdit(self)
        self.data_validade_input.setCalendarPopup(True)
        self.data_validade_input.setDate(QDate.currentDate())
        self.layout.addWidget(self.data_validade_input)

        # Botão para adicionar medicamento
        self.adicionar_btn = QPushButton("Adicionar Medicamento", self)
        self.adicionar_btn.clicked.connect(self.adicionar_medicamento)
        self.layout.addWidget(self.adicionar_btn)

        # Lista de medicamentos perto de vencer
        self.lista_medicamentos = QListWidget(self)
        self.atualizar_lista_vencimento()
        self.layout.addWidget(self.lista_medicamentos)

        # Botão para remover medicamento selecionado
        self.remover_btn = QPushButton("Remover Medicamento Selecionado", self)
        self.remover_btn.clicked.connect(self.remover_medicamento)
        self.layout.addWidget(self.remover_btn)

        # Botão para notificar reposição
        self.notificar_btn = QPushButton("Notificar Reposição", self)
        self.notificar_btn.clicked.connect(self.notificar_reposicao)
        self.layout.addWidget(self.notificar_btn)

        # Configuração da janela
        self.setLayout(self.layout)
        self.setWindowTitle("Controle de Estoque de Medicamentos")
        self.setGeometry(300, 300, 400, 400)
        self.show()

    def adicionar_medicamento(self):
        nome = self.nome_input.text()
        quantidade = self.quantidade_input.text()
        data_validade = self.data_validade_input.date().toPyDate()

        if not nome or not quantidade.isdigit():
            QMessageBox.warning(self, "Erro", "Por favor, insira um nome válido e uma quantidade numérica.")
            return

        quantidade = int(quantidade)
        medicamento = EstoqueMedicamentos(nome, quantidade, data_validade)
        self.medicamentos.append(medicamento)
        self.atualizar_lista_vencimento()

        # Limpar os campos de entrada após adicionar
        self.nome_input.clear()
        self.quantidade_input.clear()
        self.data_validade_input.setDate(QDate.currentDate())

    def remover_medicamento(self):
        current_item = self.lista_medicamentos.currentRow()
        if current_item >= 0:
            del self.medicamentos[current_item]
            self.atualizar_lista_vencimento()
        else:
            QMessageBox.warning(self, "Erro", "Selecione um medicamento para remover.")

    def atualizar_lista_vencimento(self):
        self.lista_medicamentos.clear()
        for medicamento in self.medicamentos:
            if medicamento.esta_perto_vencimento():
                dias_restantes = (medicamento.data_validade - datetime.now().date()).days
                self.lista_medicamentos.addItem(f"{medicamento.nome} - Vence em {dias_restantes} dias")

    def notificar_reposicao(self):
        medicamentos_reposicao = [med.nome for med in self.medicamentos if med.quantidade < 10]
        if medicamentos_reposicao:
            reposicao_str = "\n".join(medicamentos_reposicao)
            QMessageBox.information(self, "Notificação de Reposição", f"Medicamentos que precisam ser repostos:\n{reposicao_str}")
        else:
            QMessageBox.information(self, "Notificação de Reposição", "Nenhum medicamento precisa ser reposto no momento.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EstoqueApp()
    sys.exit(app.exec_())
