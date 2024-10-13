from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from script.backend import Cliente, Cadastro  # Importar as classes do backend

class Ui(QtWidgets.QMainWindow):
    def __init__(self, cadastro):
        super(Ui, self).__init__()
        self.cadastro = cadastro
        
        # Configuração da interface gráfica
        self.setWindowTitle('Cadastro de Clientes')

        # Mudança no tema (verde claro e branco)
        self.setStyleSheet("background-color: white; color: green;")
        
        # Botões principais
        self.cadastrar_button = QtWidgets.QPushButton('Cadastrar Cliente', self)
        self.cadastrar_button.setGeometry(50, 30, 200, 40)
        self.cadastrar_button.clicked.connect(self.exibir_campos_cadastro)

        self.verificar_button = QtWidgets.QPushButton('Buscar Cliente', self)
        self.verificar_button.setGeometry(50, 80, 200, 40)
        self.verificar_button.clicked.connect(self.verificar_cliente)

        self.total_button = QtWidgets.QPushButton('Mostrar Contador de Clientes', self)
        self.total_button.setGeometry(50, 130, 200, 40)
        self.total_button.clicked.connect(self.mostrar_total)

        # Campos de entrada (não visíveis inicialmente)
        self.nome_input = QtWidgets.QLineEdit(self)
        self.nome_input.setPlaceholderText("Nome")
        self.nome_input.setGeometry(50, 180, 200, 30)
        self.nome_input.hide()

        self.cpf_input = QtWidgets.QLineEdit(self)
        self.cpf_input.setPlaceholderText("CPF")
        self.cpf_input.setGeometry(50, 220, 200, 30)
        self.cpf_input.hide()

        self.endereco_input = QtWidgets.QLineEdit(self)
        self.endereco_input.setPlaceholderText("Endereço")
        self.endereco_input.setGeometry(50, 260, 200, 30)
        self.endereco_input.hide()

        self.cep_input = QtWidgets.QLineEdit(self)
        self.cep_input.setPlaceholderText("CEP")
        self.cep_input.setGeometry(50, 300, 200, 30)
        self.cep_input.hide()

        self.fone_input = QtWidgets.QLineEdit(self)
        self.fone_input.setPlaceholderText("Telefone")
        self.fone_input.setGeometry(50, 340, 200, 30)
        self.fone_input.hide()

        self.cadastrar_confirm_button = QtWidgets.QPushButton('Confirmar Cadastro', self)
        self.cadastrar_confirm_button.setGeometry(50, 380, 200, 40)
        self.cadastrar_confirm_button.clicked.connect(self.cadastrar_cliente)
        self.cadastrar_confirm_button.hide()

    def exibir_campos_cadastro(self):
        # Exibir campos de cadastro e botão de confirmação
        self.nome_input.show()
        self.cpf_input.show()
        self.endereco_input.show()
        self.cep_input.show()
        self.fone_input.show()
        self.cadastrar_confirm_button.show()

    def cadastrar_cliente(self):
        # Realiza o cadastro
        nome = self.nome_input.text()
        cpf = self.cpf_input.text()
        endereco = self.endereco_input.text()
        cep = self.cep_input.text()
        fone = self.fone_input.text()

        if nome and cpf and endereco and cep and fone:
            cliente = Cliente(nome, cpf, endereco, cep, fone)
            self.cadastro.cadastra(cliente)
            QMessageBox.information(self, 'Sucesso', f'Cliente {nome} cadastrado com sucesso!')
            self.limpar_campos()
        else:
            QMessageBox.warning(self, 'Erro', 'Preencha todos os campos para cadastrar o cliente.')

    def verificar_cliente(self):
        cpf, ok = QtWidgets.QInputDialog.getText(self, 'Buscar Cliente', 'Digite o CPF:')
        if ok:
            cliente = Cliente('', cpf, '', '', '')
            encontrado, mensagem = self.cadastro.verifica(cliente)

            if encontrado:
                QMessageBox.information(self, 'Resultado da Verificação', f'Cliente com CPF {cpf} foi {mensagem}.')
            else:
                QMessageBox.warning(self, 'Resultado da Verificação', f'Cliente com CPF {cpf} {mensagem}.')

    def mostrar_total(self):
        _, total_clientes = self.cadastro.total()
        QMessageBox.information(self, 'Total de Clientes', f'Total de clientes cadastrados: {total_clientes}')

    def limpar_campos(self):
        # Esconder os campos de cadastro e limpar os inputs
        self.nome_input.hide()
        self.cpf_input.hide()
        self.endereco_input.hide()
        self.cep_input.hide()
        self.fone_input.hide()
        self.cadastrar_confirm_button.hide()

        self.nome_input.clear()
        self.cpf_input.clear()
        self.endereco_input.clear()
        self.cep_input.clear()
        self.fone_input.clear()
