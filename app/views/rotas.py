from flask import Blueprint, render_template, request,jsonify

from app.models.recognizeVoice import convertAudioToText

bp = Blueprint('rotas', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/cadastro')
def login():
    return render_template('index.html')

@bp.route('/login')
def cadastro():
    return render_template('index.html')

@bp.route('/outra_rota')
def outra_rota():
    return render_template('pagina2.html')

@bp.route('/sendToTTS', methods = ['POST'])
def sendToTTS():
    convertAudioToText()
    print('transcripted')
    return 'transcripted'

@bp.route('/getFromTTS', methods = ['GET'])
def getFromTTS():
    return generateResponse()

@bp.route('/save-audio', methods=['POST'])
def save_audio():
    # Get the audio data from the request body
    audio_data = request.data

    print(audio_data)

    # Save the audio data as a WAV file
    file_path = 'app/utils/recorded_audio.wav'
    with open(file_path, 'wb') as f:
        f.write(audio_data)

    return 'Audio saved successfully', 200


