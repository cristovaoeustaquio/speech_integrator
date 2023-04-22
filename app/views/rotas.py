from flask import Blueprint, render_template

bp = Blueprint('rotas', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/outra_rota')
def outra_rota():
    return render_template('pagina2.html')
