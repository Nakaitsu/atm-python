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
    
    self.__atualizarNotas()
    strNotas = []

    for nota in self.notas:
      strNotas.append(nota.nome)  

    self.lblNotasDisponiveis.setText(" | ".join(strNotas))

    self.show()

  def __atualizarNotas(self):
    self.notas = database.getCedulas()
    self.notas = [nota for nota in self.notas if nota.quantidade > 0]


  def efetuarSaque(self, valor):
      self.__atualizarNotas()

      if self.__validarSaque(valor):
        usuario = self.session['usuario']
        self.quantidadeSaque = valor

        usuario = database.getUsuarioById(usuario.id)

        # valorCaixa = 0
        # for nota in self.notas:
        #     valorCaixa += (nota.valor * nota.quantidade)
        #     print(valorCaixa)

        resultado = ''
        qtdSaque = self.quantidadeSaque
        
        
        for nota in self.notas:
          # if qtdSaque <= valorCaixa:
          if qtdSaque >= nota.valor:
            quantidade_notas = min(qtdSaque // nota.valor, nota.quantidade)
            qtdSaque -= quantidade_notas * nota.valor
            resultado += f"Serão {quantidade_notas} de R${nota.nome}\n"
            database.atualizarCedula(nota.id, quantidade_notas, 0)

            self.lblSaque.setText(resultado)

        database.atualizarSaldoUsuario(usuario.id, usuario.saldo - self.quantidadeSaque)
        self.session['usuario'] = database.getUsuarioById(usuario.id)
        self.lblSaldo.setText(f'SEU SALDO: R${str(self.session["usuario"].saldo)}')

        self.quantidadeSaque = 0
        self.session['usuario'] = database.getUsuarioById(usuario.id)
        QMessageBox.information(self, 'SUCESSO', 'Saque efetuado!')

          # else:
          #   QMessageBox.warning(self, 'AVISO', 'Saque Invalidado!')
              
      # else:
      #   QMessageBox.warning(self, 'AVISO', 'Saque Invalidado!')

  def txtValorSaque_textChanged(self, text):
    if self.__validar():
      self.txtValorSaque.setText(text)
    else:
      self.txtValorSaque.setText(text[:-1])

  def __validarSaque(self, valorSaque) -> bool:
    self.__atualizarNotas()
    usuario = self.session['usuario']
    usuarioTemSaldo = usuario.saldo - valorSaque >= 0
    isValid = False
    saldoCaixa = 0

    temp = valorSaque
    for nota in self.notas:
      saldoCaixa += nota.quantidade * nota.valor
      if temp >= nota.valor:
        resto = temp % nota.valor
        temp = resto 

    caixaTemSaldo = valorSaque <= saldoCaixa

    # valor de saque não pode ser negativo ou 0
    # o saldo precisa ter saldo maior que o valor de saque
    # o caixa precisa ter notas
    # o saldo total do caixa precisa ser maior que o saque
    if valorSaque > 0:
          if usuarioTemSaldo:
              if len(self.notas) > 0 and caixaTemSaldo:
                  if temp == 0:
                     isValid = True
                  else:
                      QMessageBox.warning(self, 'AVISO', 'O valor não pode ser computado com as notas dispóniveis!')
              else:
                  QMessageBox.warning(self, 'AVISO', 'O Caixa não tem notas o suficiente. Contate a manutenção ou tente em outro caixa!')
          else:
              QMessageBox.warning(self, 'AVISO', 'Saldo insuficiente!')
    else:
      QMessageBox.warning(self, 'AVISO', 'O valor de saque tem que ser maior que 0!')

    return isValid

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