from Models.Cliente import Cliente
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class CadastroWindow(QMainWindow):
  def __init__(self):
    super(CadastroWindow, self).__init__()
    uic.loadUi('Views/Cadastro.ui', self)
    
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
    else:
      return False

  def btnConfirmar_Clicked(self):
    valido = self.validar()

    if valido:
      novoCliente = Cliente(
        nome = self.txtNome.text(),
        cpf = self.txtCPF.text(),
        endereco = self.txtEndereco.text(),
        senha = self.txtSenha.text(),
        saldo = float(self.txtSaldo.text())
      )

      print('novo cliente foi salvo: ', novoCliente.nome)
    else:
      print('Invalido')

  def btnLimpar_Clicked(self):
    self.txtNome.setText('')
    self.txtCPF.setText('')
    self.txtEndereco.setText('')
    self.txtSenha.setText('')
    self.txtSaldo.setText('')

  def btnCancelar_Clicked(self):
    pass