from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from AutenticarWindow import AutenticarWindow
from SaqueWindow import SaqueWindow

class MenuWindow(QMainWindow):
  def __init__(self, parent = None, session = None):
    super(MenuWindow, self).__init__(parent)
    uic.loadUi('Views/Menu.ui', self)

    self.session = session
    self.parent = parent

    self.btnSaque.clicked.connect(self.openSaque)

    if session:
      print(session)
    else:
      print('no session available')
      self.hide()
      tela = AutenticarWindow(self)

  def openSaque(self):
    self.hide()
    tela = SaqueWindow(self)
