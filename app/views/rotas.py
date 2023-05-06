import sqlite3
from app.models.database import *
from app.models.askGPT import*
from flask import Blueprint, render_template, request,jsonify

from app.models.recognizeVoice import convertAudioToText

dbFileName = 'database/database.db'
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

@bp.route('/logar', methods=['POST'])
def logar():
    data = request.get_json()
    username = data['email']
    password = data['password']
    user = searchLogin(username,password)
    if user:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'})
    
@bp.route('/cadastrar', methods = ['POST'])
def cadastrar():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')

    result = registerUser(username, email, password)
    if not result:
        return jsonify({'error': 'Username already exists'})

    return jsonify({'message': 'User registered successfully'})

@bp.route('/perguntar', methods=['POST'])
def perguntar():
    email = request.json.get('email')
    question = request.json.get('question')
    #Precisa construir a funcao para gerar a resposta em texto
    answer = 'texto recebido do openai'
    result = registerQuestion(email, question, answer)
    if result:
        return jsonify({'success': True})


