from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class MenuWindow(QMainWindow):
  def __init__(self):
    super(MenuWindow, self).__init__()

    uic.loadUi('Views/Menu.ui', self)

    self.show()
