import Helpers.database as database
from Models.Usuario import Usuario
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from CadastroWindow import CadastroWindow

class AutenticarWindow(QMainWindow):
  def __init__(self, parent = None):
    super(AutenticarWindow, self).__init__(parent)
    uic.loadUi('Views/Autenticar.ui', self)

    self.parent = parent

    self.btnConfirmar.clicked.connect(self.btnConfirmar_Clicked)
    self.btnLimpar.clicked.connect(self.btnLimpar_Clicked)
    self.btnCadastrar.clicked.connect(self.btnCadastrar_Clicked)

    self.show()

  def __validar(self):
    cpf = self.txtCPF.text()
    senha = self.txtSenha.text()

    return cpf and senha

  def btnConfirmar_Clicked(self):
    try:
      if self.__validar():
        usuario = database.getUsuario(
          cpf = self.txtCPF.text(),
          senha = self.txtSenha.text()
        )

        if usuario.id:
          self.parent.session = {'usuario': usuario}
          self.__limparTela()
          self.close()
          self.parent.show()
        else:
          QMessageBox.warning(self, 'ERRO', 'Erro de autenticação!')
      
      else:
        QMessageBox.warning(self, 'AVISO', 'Preencha todos os campos!')

    except Exception as e:
      QMessageBox.warning(self, 'ERRO', e.message)

  def btnLimpar_Clicked(self):
    self.__limparTela()

  def __limparTela(self):
    self.txtCPF.setText('')
    self.txtSenha.setText('')

  def btnCadastrar_Clicked(self):
    self.__limparTela()
    self.hide()
    tela = CadastroWindow(self)