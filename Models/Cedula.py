class Cedula:
  def __init__(self, nome, valor, quantidade = None, id = None):
    self.id = id
    self.nome = nome
    self.quantidade = quantidade
    self.valor = valor