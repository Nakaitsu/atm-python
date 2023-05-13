class Cliente:
  def __init__(self, nome, cpf, endereco, senha, saldo, id = None):
    self.nome = nome
    self.cpf = cpf
    self.endereco = endereco
    self.senha = senha
    self.saldo = saldo
    self.id = id