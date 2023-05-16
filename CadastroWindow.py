import Helpers.database as database
from Models.Usuario import Usuario
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class CadastroWindow(QMainWindow):
  def __init__(self, parent = None):
    super(CadastroWindow, self).__init__(parent)
    uic.loadUi('Views/Cadastro.ui', self)

    self.parent = parent
    
    self.btnConfirmar.clicked.connect(self.btnConfirmar_Clicked)
    self.btnLimpar.clicked.connect(self.btnLimpar_Clicked)
    self.btnCancelar.clicked.connect(self.btnCancelar_Clicked)

    self.show()

  def validar(self):
    nome = self.txtNome.text(),
    cpf = self.txtCPF.text(),
    endereco = self.txtEndereco.text(),
    senha = self.txtSenha.text(),
    saldo = float(self.txtSaldo.text())

    if nome and cpf and endereco and senha and saldo:
      try:
        float(saldo)
        return True
      except ValueError:
        return False
    
    return False

  def btnConfirmar_Clicked(self):
    if self.validar():
      novoUsuario = Usuario(
        nome = self.txtNome.text(),
        cpf = self.txtCPF.text(),
        endereco = self.txtEndereco.text(),
        senha = self.txtSenha.text(),
        saldo = float(self.txtSaldo.text())
      )

      database.addUsuario(novoUsuario)
      self.__limparTela()

      print('novo cliente foi salvo: ', novoUsuario.nome)
    else:
      print('Inválido')

  def btnLimpar_Clicked(self):
    self.__limparTela()

  def btnCancelar_Clicked(self):
    self.close()
    self.parent.show()

  def __limparTela(self):
    self.txtNome.setText('')
    self.txtCPF.setText('')
    self.txtEndereco.setText('')
    self.txtSenha.setText('')
    self.txtSaldo.setText('')

