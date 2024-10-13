import sys
from PyQt5 import QtWidgets
from script.backend import Cadastro
from ui.frontend import Ui

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    # Inicializa a lógica de cadastro
    cadastro = Cadastro()

    # Cria e mostra a interface gráfica
    janela = Ui(cadastro)
    janela.setGeometry(50, 100, 300, 400)
    janela.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
