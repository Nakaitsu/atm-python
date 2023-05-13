import Helpers.database as database
from CadastroWindow import CadastroWindow
from PyQt5.QtWidgets import QApplication

def appStartup():
  database.start()
  
  app = QApplication([])
  window = CadastroWindow()
  app.exec_()

if __name__ == '__main__':
  appStartup()