import mysql.connector
from Models.Usuario import Usuario
from Models.Cedula import Cedula

def start() -> None:
  conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '235711',
    auth_plugin = 'mysql_native_password'
  )

  cursor = conn.cursor()

  with open('SQL/startup.sql', 'r') as comando:
    query = comando.read()

  cursor.execute(query)
  conn.close()

def getConexao():
  return mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '235711',
    database = 'caixa_eletronico',
    auth_plugin = 'mysql_native_password'
  )

## USUARIO ######

def addUsuario(usuario):
  with open('SQL/insertUsuario.sql', 'r') as comando:
    query = comando.read()

  conn = getConexao()

  cursor = conn.cursor()
  values = (usuario.nome, usuario.cpf, usuario.endereco, usuario.senha, usuario.saldo)
  cursor.execute(query, values)
  conn.commit()  
  
  conn.close()

def getUsuario(cpf, senha):
  with open('SQL/selectUsuario.sql', 'r') as comando:
    query = comando.read()

  usuario = Usuario()

  conn = getConexao()

  cursor = conn.cursor()
  cursor.execute(query, (cpf, senha))
  dados = cursor.fetchone()

  usuario.id = dados[0]
  usuario.nome = dados[1]
  usuario.cpf = dados[2]
  usuario.endereco = dados[3]
  usuario.senha = dados[4]
  usuario.saldo = dados[5]

  conn.close()
  
  return usuario

def getUsuarioById(idUsuario):
  query = f'SELECT * FROM users WHERE id = {idUsuario}'

  usuario = Usuario()

  conn = getConexao()

  cursor = conn.cursor()
  cursor.execute(query)
  dados = cursor.fetchone()

  usuario.id = dados[0]
  usuario.nome = dados[1]
  usuario.cpf = dados[2]
  usuario.endereco = dados[3]
  usuario.senha = dados[4]
  usuario.saldo = dados[5]

  conn.close()

  return usuario

def atualizarSaldoUsuario(idUsuario, novoSaldo) -> None:
  query = f'UPDATE users SET saldo = {novoSaldo} WHERE id = {idUsuario}'

  conn = getConexao()

  cursor = conn.cursor()
  cursor.execute(query)
  conn.commit()

  conn.close()

## CEDULAS ######

def getCedulas():
  query = 'SELECT * FROM cedulas'

  conn = getConexao()

  cursor = conn.cursor()
  cursor.execute(query)
  cedulas = cursor.fetchall()

  listaCedulas = []

  for c in cedulas:
    cedula = Cedula(
      id = c[0],
      nome = c[1],
      valor = c[2],
      quantidade = c[3]
    )

    listaCedulas.append(cedula)

  conn.close()

  return listaCedulas

def atualizarCedula(idCedula, quantiade) -> None:
  query = f'UPDATE cedulas SET quantidade = {quantiade} WHERE id = {idCedula}'

  conn = getConexao()

  cursor = conn.cursor()
  cursor.execute(query)
  conn.commit()

  conn.close()

# for nota in reversed(notas):
  # if int(self.valor) >= nota:
  #     quantidade_notas = int(self.valor) // nota
  #     resultado += f"Serão {quantidade_notas} de R${nota}\n"
  #     self.valor = int(self.valor) % nota