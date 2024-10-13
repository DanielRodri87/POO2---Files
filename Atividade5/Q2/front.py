import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QMessageBox
from back import Bicicleta

class AluguelBicicletaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.bicicletas = [
            Bicicleta("Modelo A", 10, 0),
            Bicicleta("Modelo B", 15, 0),
            Bicicleta("Modelo C", 20, 0)
        ]
        self.initUI()

    def initUI(self):
        # Layout principal
        self.layout = QVBoxLayout()

        # Campo para selecionar bicicleta
        self.bicicleta_input = QComboBox(self)
        for bike in self.bicicletas:
            self.bicicleta_input.addItem(bike.modelo)
        self.layout.addWidget(self.bicicleta_input)

        # Campo para inserir quantidade de horas
        self.horas_input = QLineEdit(self)
        self.horas_input.setPlaceholderText("Digite o número de horas de aluguel")
        self.layout.addWidget(self.horas_input)

        # Botão para calcular tarifa
        self.calcular_btn = QPushButton("Calcular Tarifa", self)
        self.calcular_btn.clicked.connect(self.calcular_tarifa)
        self.layout.addWidget(self.calcular_btn)

        # Botão para confirmar aluguel
        self.confirmar_btn = QPushButton("Confirmar Aluguel", self)
        self.confirmar_btn.clicked.connect(self.confirmar_aluguel)
        self.layout.addWidget(self.confirmar_btn)

        # Campo para exibir resultado
        self.resultado_label = QLabel(self)
        self.layout.addWidget(self.resultado_label)

        # Campo para exibir status
        self.status_label = QLabel(self)
        self.atualizar_status_bicicletas()
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)
        self.setWindowTitle("Aluguel de Bicicletas")
        self.setGeometry(100, 100, 400, 300)
        self.show()

    def calcular_tarifa(self):
        try:
            horas = int(self.horas_input.text())
            bicicleta_selecionada = self.bicicletas[self.bicicleta_input.currentIndex()]
            tarifa = bicicleta_selecionada.calcular_tarifa(horas)
            self.resultado_label.setText(f"Valor Total: R$ {tarifa:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido de horas.")

    def confirmar_aluguel(self):
        bicicleta_selecionada = self.bicicletas[self.bicicleta_input.currentIndex()]
        if bicicleta_selecionada.alugada == 0:
            bicicleta_selecionada.alugada = 1
            QMessageBox.information(self, "Sucesso", "Aluguel confirmado!")
            self.atualizar_status_bicicletas()
        else:
            QMessageBox.warning(self, "Erro", "Essa bicicleta já está alugada.")

    def atualizar_status_bicicletas(self):
        status = "Status das Bicicletas:\n"
        for bike in self.bicicletas:
            status += f"{bike.modelo} - {'Disponível' if bike.alugada == 0 else 'Alugada'}\n"
        self.status_label.setText(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AluguelBicicletaApp()
    sys.exit(app.exec_())
