from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from AutenticarWindow import AutenticarWindow
from SaqueWindow import SaqueWindow
from ManutencaoWindow import ManutencaoWindow

class MenuWindow(QMainWindow):
  def __init__(self, parent = None, session = None):
    super(MenuWindow, self).__init__(parent)
    uic.loadUi('Views/Menu.ui', self)

    self.session = session
    self.parent = parent

    self.btnSaque.clicked.connect(self.openSaque)
    self.btnSair.clicked.connect(self.encerrarSessao)
    # self.btnManutencao.clicked.connect(self.openManutencao)

    # if not self.session.usuario.isAdmin:
    #   self.btnManutencao.hide()

    if session:
      print(session)
      self.show()
    else:
      print('no session available')
      self.hide()
      tela = AutenticarWindow(self)

  def openSaque(self):
    self.hide()
    tela = SaqueWindow(self)

  def openManutencao(self):
    self.hide()
    tela = ManutencaoWindow(self)

  def encerrarSessao(self):
    self.session = None
    self.hide()
    tela = AutenticarWindow(self)