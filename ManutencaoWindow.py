import Helpers.database as database
# from Models.Cedula import Cedula
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class ManutencaoWindow(QMainWindow):
  def __init__(self, parent = None, session = None):
    super(ManutencaoWindow, self).__init__(parent)
    uic.loadUi('Views/Manutencao.ui', self)

    self.parent = parent
    self.session = session
    self.cedulas = database.getCedulas()

    self.btnNext.clicked.connect(self.btnNext_Clicked)
    self.btnPrev.clicked.connect(self.btnPrev_Clicked)
    self.btnAdd.clicked.connect(self.btnAdd_Clicked)
    self.btnConfirmar.clicked.connect(self.btnConfirmar_Clicked)

    self.btnPrev.setEnabled(False)

    if not self.cedulas.count() > 1:
      self.btnNext.setEnabled(False)

    self.cedulaAtual = self.cedulas[0]
    self.show()

  def btnNext_Clicked(self):
    self.cedulaAtual = self.cedulas[self.cedulas.index(self.cedulaAtual) + 1]
    self.lblNomeCedula.setText(self.cedulaAtual.nome)
    self.btnPrev.setEnabled(True)

    if self.cedulas.index(self.cedulaAtual) >= self.cedulas.count():
      self.btnNext.setEnabled(False)

  def btnPrev_Clicked(self):
    self.cedulaAtual = self.cedulas[self.cedulas.index(self.cedulaAtual) - 1]
    self.lblNomeCedula.setText(self.cedulaAtual.nome)
    self.btnNext.setEnabled(True)

    if self.cedulas.index(self.cedulaAtual) <= 0:
      self.btnPrev.setEnabled(False)

  def btnAdd_Clicked(self): # form para adicionar a cedula (nome, quantidade, valor)
    pass

  def btnConfirmar_Clicked(self):
    if self.__validar():
      database.atualizarCedula(self.cedulaAtual.id, int(self.txtQuantidade))

  def __validar(self) -> bool:
    try:
      quantidade = int(self.txtQuantidade)
      return True
    except:
      return False