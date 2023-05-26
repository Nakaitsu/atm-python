import Helpers.database as database
from Models.Usuario import Usuario
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox

class CadastroWindow(QMainWindow):
  def __init__(self, parent = None):
    super(CadastroWindow, self).__init__(parent)
    uic.loadUi('Views/Cadastro.ui', self)

    self.parent = parent
    
    self.btnConfirmar.clicked.connect(self.btnConfirmar_Clicked)
    self.btnLimpar.clicked.connect(self.btnLimpar_Clicked)
    self.btnCancelar.clicked.connect(self.btnCancelar_Clicked)

    self.show()

  def __validar(self):
    try:
      nome = self.txtNome.text(),
      cpf = int(self.txtCPF.text()),
      endereco = self.txtEndereco.text(),
      senha = self.txtSenha.text(),
      saldo = int(self.txtSaldo.text())

      if nome and cpf and endereco and senha and saldo > 0:
        if not database.UsuarioExiste(self.txtCPF.text()):
          return True
      
      return False
    
    except:
      return False

  def btnConfirmar_Clicked(self):
    if self.__validar():
      saldo = float(self.txtSaldo.text())

      if saldo > 0 and saldo <= 20000:  
        novoUsuario = Usuario(
          nome = self.txtNome.text(),
          cpf = self.txtCPF.text(),
          endereco = self.txtEndereco.text(),
          senha = self.txtSenha.text(),
          saldo = float(self.txtSaldo.text())
        )

        database.addUsuario(novoUsuario)
        QMessageBox.information(self, 'SUCESSO', 'Cadastro efetuado com sucesso!')
        
        self.__limparTela()
        self.close()
        self.parent.show()
      else:
        QMessageBox.warning(self, 'ERRO', 'O deposito tem que ser positivo e não pode ser maior que R$20000!')
    
    else:
      QMessageBox.warning(self, 'ERRO', 'Cadastro inválido!')

  def btnLimpar_Clicked(self):
    self.__limparTela()

  def btnCancelar_Clicked(self):
    self.__limparTela()
    self.close()
    self.parent.show()

  def __limparTela(self):
    self.txtNome.setText('')
    self.txtCPF.setText('')
    self.txtEndereco.setText('')
    self.txtSenha.setText('')
    self.txtSaldo.setText('')

