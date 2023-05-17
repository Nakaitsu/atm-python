from MenuWindow import MenuWindow
from PyQt5.QtWidgets import QApplication
import Helpers.database as database

def appStartup():
  database.start()
  
  app = QApplication([])
  window = MenuWindow()
  app.exec_()

if __name__ == '__main__':
  appStartup()