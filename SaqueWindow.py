import Helpers.database as database
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic

class SaqueWindow(QMainWindow):
  def __init__(self, parent = None, session = None):
    super(SaqueWindow, self).__init__(parent)
    uic.loadUi('Views/Saque.ui', self)

    self.parent = parent
    self.session = parent.session
    self.quantidadeSaque = 0

    self.btnConfirmar.clicked.connect(self.btnConfirmar_Clicked)
    self.btnCancelar.clicked.connect(self.btnCancelar_Clicked)
    self.btnLimpar.clicked.connect(self.btnLimpar_Clicked)
    self.btn20.clicked.connect(lambda: self.efetuarSaque(20))
    self.btn50.clicked.connect(lambda: self.efetuarSaque(50))
    self.btn100.clicked.connect(lambda: self.efetuarSaque(100))
    self.btn150.clicked.connect(lambda: self.efetuarSaque(150))
    self.txtValorSaque.textChanged.connect(self.txtValorSaque_textChanged)
    self.lblSaldo.setText(f'SEU SALDO: R$ {str(self.session["usuario"].saldo)}')
    
    strNotas = []

    for nota in database.getCedulas():
      strNotas.append(nota.nome)  

    self.lblNotasDisponiveis.setText(" | ".join(strNotas))

    self.show()

  def efetuarSaque(self, valor):
    if self.__validarSaque(valor):
      usuario = self.session['usuario']
      self.quantidadeSaque = valor

      self.session['usuario'] = database.getUsuarioById(usuario.id)

      notas = database.getCedulas()
      notas = [nota for nota in notas if nota.quantidade > 0]

      resultado = ''
      qtdSaque = self.quantidadeSaque
      
      saqueValido = False
      
      for nota in notas:
        if qtdSaque % nota.valor == 0:
          saqueValido = True

      if saqueValido: 
        if usuario.saldo >= qtdSaque:
          for nota in notas:
            if qtdSaque >= nota.valor and nota.quantidade > 0:
              quantidade_notas = qtdSaque // nota.valor
              resultado += f"Serão {quantidade_notas} de R${nota.nome}\n"
              qtdSaque = qtdSaque % nota.valor
              database.atualizarCedula(nota.id, quantidade_notas, 0)

          self.lblSaque.setText(resultado)

          database.atualizarSaldoUsuario(usuario.id, usuario.saldo - self.quantidadeSaque, 0)
          self.lblSaldo.setText(f'SEU SALDO: R${str(self.session["usuario"].saldo)}')
          self.session['usuario'] = database.getUsuarioById(usuario.id)

          self.quantidadeSaque = 0
          QMessageBox.information(self, 'SUCESSO', 'Saque efetuado!')
          
        else:
          QMessageBox.information(self, 'ERROR', 'Saldo insuficiente!')
      else:
        QMessageBox.warning(self, 'ERROR', 'Valor de saque inválido!')

    else:
      QMessageBox.warning(self, 'AVISO', 'Saque Invalidado!')

  def txtValorSaque_textChanged(self, text):
    if self.__validar():
      self.txtValorSaque.setText(text)
    else:
      self.txtValorSaque.setText(text[:-1])

  def __validarSaque(self, valorSaque) -> bool:
    usuario = self.session['usuario']
    usuarioTemSaldo = usuario.saldo - valorSaque > 0

    if valorSaque > 0 and usuarioTemSaldo:
      return True
    
    return False

  def __validar(self) -> bool:
    try:
      self.quantidadeSaque = int(self.txtValorSaque.text())
      return True
    except:
      return False

  def btnConfirmar_Clicked(self):
    if self.__validar():
      self.efetuarSaque(int(self.txtValorSaque.text()))

  def btnCancelar_Clicked(self):
    self.__limparTela()
    self.close()
    self.parent.show()
  
  def btnLimpar_Clicked(self):
    self.__limparTela()

  def __limparTela(self):
    self.txtValorSaque.setText('')