from flask import Flask
#from config import Config

def create_app():
    app = Flask(__name__)
#    app.config.from_object(Config)

    from app.views.rotas import bp as bp_rotas
    app.register_blueprint(bp_rotas)

#    from app.models.arquivo1 import ClasseModelo1

    return app
