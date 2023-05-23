import Helpers.database as database
from Models.Cedula import Cedula
from PyQt5 import uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QMessageBox

class ManutencaoWindow(QMainWindow):
  def __init__(self, parent = None, session = None):
    super(ManutencaoWindow, self).__init__(parent)
    uic.loadUi('Views/Manutencao.ui', self)

    self.parent = parent
    self.session = session

    self.btnVoltar.clicked.connect(self.btnVoltar_Clicked)
    self.btnConfirmarReposicao.clicked.connect(self.btnConfirmarReposicao_Clicked)
    self.btnConfirmarCadastro.clicked.connect(self.btnConfirmarCadastro_Clicked)
    self.btnNotificacoes.clicked.connect(self.btnNotificacoes_Clicked)
    
    self.__notificarCedulasEmFalta()
    self.__atualizar()

    self.show()

  def __notificarCedulasEmFalta(self):
    self.notificacoes = []

    for cedula in  database.getCedulasEmFalta():
      self.notificacoes.append(f'A cédula de R${cedula.nome} está em falta!')

    if len(self.notificacoes) > 0:
      self.btnNotificacoes.setText(f'Notificações ({len(self.notificacoes)})')
    else:
      self.btnNotificacoes.setText('Notificações')

  def __atualizar(self):
    self.cbbReposicaoNota.clear()
    self.cedulas = database.getCedulas()
    
    notasModel = QStandardItemModel()

    for nota in self.cedulas:
      item = QStandardItem(f'{nota.quantidade} notas de R${nota.nome} disponívies')
      notasModel.appendRow(item)

      self.cbbReposicaoNota.addItem(nota.nome, nota.id)

    self.lsvNotas.setModel(notasModel)
    self.__notificarCedulasEmFalta()

  def btnNotificacoes_Clicked(self):
    if len(self.notificacoes) > 0:
      QMessageBox.information(self, self.btnNotificacoes.text(), "\n".join(self.notificacoes))
    else:
      QMessageBox.information(self, 'VAZIO', 'Nenhuma notificação!')

  def btnConfirmarCadastro_Clicked(self):
    try:
      nome = self.txtCadastroNome.text()
      valor = int(self.txtCadastroValor.text())
      quantidade = int(self.spbCadastroQuantidade.text())
      
      if self.__validarCadastro():
        novaCedula = Cedula(nome, valor, quantidade)
        
        cedulaExistente = None
        for cedula in self.cedulas:
          if cedula.valor == valor:
            cedulaExistente = cedula
        
        if cedulaExistente:
          database.atualizarCedula(cedulaExistente.id, quantidade, 1)
        else:
          database.addCedula(novaCedula)
        
        self.__atualizar()
        self.__limparTela()

        QMessageBox.information(self, 'SUCESSO', 'Nova cédula cadastrada!')
      else:
        QMessageBox.warning(self, 'ERROR', 'O cadastro possui erro!')

    except Exception as e:
      QMessageBox.warning(self, 'ERROR', str(e))

  def __validarCadastro(self):
    try:
      nome = self.txtCadastroNome.text()
      valor = int(self.txtCadastroValor.text())
      quantidade = self.spbCadastroQuantidade.value()

      if nome and valor and quantidade > 0:
        return True

      return False
    except:
      return False

  def __limparTela(self):
    self.txtCadastroNome.setText('')
    self.txtCadastroValor.setText('')
    self.spbCadastroQuantidade.setValue(0)
    self.cbbReposicaoNota.setCurrentIndex(0)
    self.spbReposicaoQuantidade.setValue(0)

  def btnVoltar_Clicked(self):
    self.close()
    self.__limparTela()
    self.parent.show()

  def btnConfirmarReposicao_Clicked(self):
    database.atualizarCedula(int(self.cbbReposicaoNota.currentData()), self.spbReposicaoQuantidade.value(), True)
    self.__atualizar()
    self.__limparTela()
    
    QMessageBox.information(self, 'SUCESSO', 'Reposição efetuada com sucesso!')