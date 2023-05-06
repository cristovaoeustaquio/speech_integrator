import numpy as np
import pandas as pd
import sqlite3
import json
import io

dbFileName = 'database/database.db'

#Verificação de login

def loginVerification(rows):
    if rows == 0:
        return False
    else:
        return True


def getUsername(email):
    with sqlite3.connect(dbFileName) as conn:
        cursor = conn.cursor()
        sql = "SELECT username FROM usuarios WHERE email=?"
        cursor.execute(sql, (email,))
        username = cursor.fetchall()
        return username

def searchLogin(email, password):
  with sqlite3.connect(dbFileName) as conn:
    cursor = conn.cursor()
    sql = "SELECT email, password FROM usuarios WHERE email=? AND password=?"
    cursor.execute(sql, (email, password))
    rows = cursor.fetchall()
    rows=np.array(rows)
    loginExist = loginVerification(rows.shape[0])
  return loginExist

#Registro de usuario

def registerUser(username, email, password):
  with sqlite3.connect(dbFileName) as conn:
        cursor = conn.cursor()
        query = 'SELECT email FROM usuarios WHERE email = ?'
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        if result:
            return False
        query = 'INSERT INTO usuarios (username, email, password) VALUES (?, ?, ?)'
        cursor.execute(query, (username, email, password))
        conn.commit()
        return True

def registerQuestion(email, question, answer):
  with sqlite3.connect(dbFileName) as conn:
        cursor = conn.cursor()
        query = 'INSERT INTO perguntas_e_respostas (email, question, answer) VALUES (?, ?, ?)'
        cursor.execute(query, (email, question, answer))
        conn.commit()
        return True

def viewChat(email):
  with sqlite3.connect(dbFileName) as conn:
        cursor = conn.cursor()
        chat = 'SELECT question AND answer FROM perguntas_e_respostas WHERE email = ?'
        chat = chat.to_numpy()
        return chat

def create_db():
  conn = sqlite3.connect(dbFileName)
  # Criar a tabela de usuários
  conn.execute('''CREATE TABLE usuarios
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT NOT NULL,
             email TEXT NOT NULL,
             password TEXT NOT NULL);''')
  
  conn.execute('''CREATE TABLE perguntas_e_respostas
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             email TEXT NOT NULL,
             question TEXT NOT NULL,
             answer TEXT NOT NULL);''')
  
  # Salvar as alterações no banco de dados
  conn.commit()
  # Fechar a conexão com o banco de dados
  conn.close()

#Main
#print(registerUser('teste2', 'teste2@gmail.com', 'teste123'))
#print(searchLogin('teste@gmail.com','teste123'))
#registerQuestion('teste2@gmail.com', 'no ceu tem pao2', 'nao sei2')

