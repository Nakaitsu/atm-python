import Helpers.database as database
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from CadastroWindow import CadastroWindow

class AutenticarWindow(QMainWindow):
  def __init__(self, parent = None):
    super(AutenticarWindow, self).__init__(parent)
    uic.loadUi('Views/Autenticar.ui', self)

    self.parent = parent

    self.btnConfirmar.clicked.connect(self.btnConfirmar_Clicked)
    self.btnLimpar.clicked.connect(self.btnLimpar_Clicked)
    self.btnCancelar.clicked.connect(self.btnCancelar_Clicked)
    self.btnCadastrar.clicked.connect(self.btnCadastrar_Clicked)

    self.show()

  def validar(self):
    cpf = self.txtCPF.text()
    senha = self.txtSenha.text()

    return cpf and senha

  def btnConfirmar_Clicked(self):
    if self.validar():
      usuario = database.getUsuario(
        cpf = self.txtCPF.text(),
        senha = self.txtSenha.text()
      )

      if usuario:
        print('logado')

        self.close()
        self.parent.show()
      else:
        print('erro de autenticacao')
      
    else:
      print('Inválido')

  def btnLimpar_Clicked(self):
    self.__limparTela()

  def btnCancelar_Clicked(self):
    pass

  def __limparTela(self):
    self.txtCPF.setText('')
    self.txtSenha.setText('')

  def btnCadastrar_Clicked(self):
    self.hide()
    tela = CadastroWindow(self)