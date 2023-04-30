from flask import Blueprint, render_template

from app.models.recognizeVoice import convertAudioToText

bp = Blueprint('rotas', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/outra_rota')
def outra_rota():
    return render_template('pagina2.html')


@bp.route('/sendToTTS', methods = ['POST'])
def sendToTTS():
    audio = request.get_json()['audio']
    convertAudioToText(audio)
    return render_template('pagina2.html')

@bp.route('/getFromTTS', methods = ['POST'])
def sendToTTS():
    audio = request.get_json()['audio']
    convertAudioToText(audio)
    return 'transcripted'