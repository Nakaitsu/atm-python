from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from AutenticarWindow import AutenticarWindow
from SaqueWindow import SaqueWindow

class MenuWindow(QMainWindow):
  def __init__(self, parent = None, sessao = None):
    super(MenuWindow, self).__init__(parent)
    uic.loadUi('Views/Menu.ui', self)

    self.sessao = sessao
    self.parent = parent

    self.btnSaque.clicked.connect(self.openSaque)

    if sessao:
      print(sessao)
    else:
      print('no session available')
      self.hide()
      tela = AutenticarWindow(self)

  def openSaque(self):
    self.hide()
    tela = SaqueWindow(self)
