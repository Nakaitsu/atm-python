from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class SaqueWindow(QMainWindow):
  def __init__(self, parent = None):
    super(SaqueWindow, self).__init__(parent)
    uic.loadUi('Views/Saque.ui', self)

    self.parent = parent
    self.quantidadeSaque = 0

    self.btn20.clicked.connect(lambda: self.addValorSaque(20))
    self.btn50.clicked.connect(lambda: self.addValorSaque(50))
    self.btn100.clicked.connect(lambda: self.addValorSaque(100))
    self.btn150.clicked.connect(lambda: self.addValorSaque(150))

    self.show()

  def addValorSaque(self, valor):
    self.quantidadeSaque += valor
    self.txtValorSaque.setText(str(self.quantidadeSaque))

  def validar(self):
    pass

  def btnConfirmar_Clicked(self):
    pass

  def btnCancelar_Clicked(self):
    self.__limparTela()
    self.close()
    self.parent.show()
  
  def btnLimpar_Clicked(self):
    self.__limparTela()

  def __limparTela(self):
    pass