import numpy as np
import pandas as pd
import sqlite3
import json
import io

#Verificação de login

def loginVerification(rows):
    if rows == 0:
        return False
    else:
        return True

def searchLogin(user, password):
  with sqlite3.connect('database/database.db') as conn:
    cursor = conn.cursor()
    sql = "SELECT user, password FROM usuarios WHERE user=? AND password=?"
    cursor.execute(sql, (user, password))
    rows = cursor.fetchall()
    rows=np.array(rows)
    print(conn)
    conn.close()
    loginExist = loginVerification(rows.shape[0])
  return loginExist

#Registro de login

def registerLogin(user, email, password):
  with sqlite3.connect('database/database.db') as conn:
    cursor = conn.cursor()
    sql = "INSERT INTO usuarios (user, email, password) VALUES (?, ?, ?)"
    stmt = cursor.execute(sql, (user, email, password))
    while True:
      res = stmt.fetchone()
      if res is None:
        break

def create_db():
  conn = sqlite3.connect('database/database.db')
  # Criar a tabela de usuários
  conn.execute('''CREATE TABLE usuarios
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             user TEXT NOT NULL,
             email TEXT NOT NULL,
             password TEXT NOT NULL);''')
  # Salvar as alterações no banco de dados
  conn.commit()
  # Fechar a conexão com o banco de dados
  conn.close()

#Main
"""
if 'button' == 'buttonRequest':
    user = loginInfo['user']
    password = loginInfo['password']
    loginExist = searchLogin(user, password)
    print(loginExist)

if 'button' == 'buttonRegister':
    user = loginInfo['user']
    email = loginInfo['email']
    password = loginInfo['password']
    registerLogin(user, email, password)
"""
