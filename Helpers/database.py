import mysql.connector

def start():
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

  conn = getConexao()

  cursor = conn.cursor()
  cursor.execute(query, (cpf, senha))
  usuario = cursor.fetchone()
  conn.close()
  
  return usuario