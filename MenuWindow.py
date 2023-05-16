from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from AutenticarWindow import AutenticarWindow
from CadastroWindow import CadastroWindow

class MenuWindow(QMainWindow):
  def __init__(self, parent = None, sessao = None):
    super(MenuWindow, self).__init__(parent)
    uic.loadUi('Views/Menu.ui', self)

    self.sessao = sessao
    self.parent = parent

    if sessao:
      print(sessao)
    else:
      print('no session available')
      tela = AutenticarWindow(self)
      self.hide()
