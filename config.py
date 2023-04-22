import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'minha_chave_secreta'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///meu_banco_de_dados.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
