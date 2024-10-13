# Crie uma classe Usuario que depende da abstração Notificacao para enviar mensagens.
# Implemente as classes NotificacaoEmail e NotificacaoSMS que enviam notificações de
# diferentes formas. A classe Usuario deve ter um método enviar_notificacao e usar
# métodos getter e setter para definir a mensagem através de @propert

from abc import ABC, abstractmethod

class Notificacao(ABC):
    """
    Interface que define o método para enviar notificações.
    """
    @abstractmethod
    def enviar(self, mensagem):
        """
        Método abstrato para envio da notificação.
        """
        pass

class NotificacaoEmail(Notificacao):
    """
    Classe que implementa o envio de notificações via Email.
    """
    def enviar(self, mensagem):
        print(f"Enviando e-mail: {mensagem}")

class NotificacaoSMS(Notificacao):
    """
    Classe que implementa o envio de notificações via SMS.
    """
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

class Usuario:
    """
    Classe que representa um usuário e utiliza uma abstração de Notificacao
    para enviar mensagens.
    """

    def __init__(self, nome):
        self.nome = nome
        self._mensagem = ""
        self._notificacao = None  

    @property
    def mensagem(self):
        """
        Getter para acessar a mensagem.
        """
        return self._mensagem

    @mensagem.setter
    def mensagem(self, msg):
        """
        Setter para definir a mensagem.
        """
        self._mensagem = msg

    def set_notificacao(self, notificacao: Notificacao):
        """
        Define o tipo de notificação a ser usada
        """
        self._notificacao = notificacao

    def enviar_notificacao(self):
        """
        Envia a notificação usando o método da interface Notificacao.
        """
        if self._notificacao:
            self._notificacao.enviar(self.mensagem)
        else:
            print("Nenhum tipo de notificação foi definido.")


usuario = Usuario("Daniel")

usuario.mensagem = "Sua conta foi aprovada!"

usuario.set_notificacao(NotificacaoEmail())
usuario.enviar_notificacao()  

usuario.set_notificacao(NotificacaoSMS())
usuario.enviar_notificacao()  
