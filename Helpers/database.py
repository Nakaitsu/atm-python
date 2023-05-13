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
  pass