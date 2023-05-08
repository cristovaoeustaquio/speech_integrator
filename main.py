from PySide6.QtWidgets import QApplication, QMainWindow,QFileDialog

from ui_main import Ui_MainWindow

from PySide6.QtCore import Qt, QByteArray, QIODevice

from PySide6.QtMultimedia import QAudioFormat, QAudioInput

from database import *

from classes import *

from PySide6.QtMultimedia import QAudio, QAudioFormat, QAudioInput

from audio import AudioRecorder

import threading

from PySide6.QtCore import QByteArray, QIODevice, QMargins, QRect, Qt, Signal, Slot, QStandardPaths,QFile,QTimer

from PySide6.QtGui import QPainter, QPalette

from PySide6.QtMultimedia import (    QAudio,    QAudioDevice,    QAudioFormat,    QAudioSource,    QMediaDevices,)

from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,QLabel, QPlainTextEdit, QPushButton, QRadioButton,QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,QWidget,QFileDialog)

from PySide6.QtMultimedia import QAudioInput

from PySide6.QtMultimedia import QSoundEffect

import pyaudio

import wave

from models.recognizeVoice import convertAudioToText

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.logarButton.clicked.connect(self.logar)
        self.ui.cadastroButton.clicked.connect(self.changePageToCadastro)
        self.ui.cadastrarUserButton.clicked.connect(self.cadastro)
        self.ui.recordAudioButton.clicked.connect(self.toggle_recording)
        self.ui.logarButton_2.clicked.connect(self.changePageToLogar)
        
        self.sound_effect = QSoundEffect()
        # Load the background image
        self.ui.speechLabel.setStyleSheet("background-image:url(utils/AudioWave.png)")
        
        # Set up PyAudio
        self.audio = pyaudio.PyAudio()
        self.is_recording = False
        self.frames = []
        self.sample_rate = 16000
        self.channels = 1
        self.format = pyaudio.paInt16
        
        # Set the timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_timeout)
        
    def toggle_recording(self):

        chat=[]

        if not self.is_recording:
            self.is_recording = True
            self.frames = []
            threading.Thread(target=self.record).start()
            self.ui.recordAudioButton.setText("Stop")
        else:
            self.is_recording = False
            threading.Thread(target=self.save).start()
            self.ui.recordAudioButton.setText("Record")
            self.ui.recordAudioButton.setEnabled(False)
            
            user,chatText,file = convertAudioToText()
            

            newUser = userWidget(self.ui.widgetChatArea)
            self.ui.verticalLayout_2.addWidget(newUser)
            newUser.labelTextUser.setText(user)
            chat.append(user)

            newUser2 = AIWidget(self.ui.widgetChatArea)
            self.ui.verticalLayout_2.addWidget(newUser2)
            newUser2.labelTextAI.setText(chatText)
            chat.append(chatText)

            registerQuestion(self.ui.emailLineEdit.text(),chat[0],chat[1])

            self.ui.recordAudioButton.setEnabled(True)

    def record(self):
        self.stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=1024
        )
        while self.is_recording:
            data = self.stream.read(1024)
            self.frames.append(data)
        
    def save(self):
        
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        filename = "output.wav"
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        
        # Set up PyAudio
        self.audio = pyaudio.PyAudio()
        self.is_recording = False
        self.frames = []
        self.sample_rate = 16000
        self.channels = 1
        self.format = pyaudio.paInt16

    def logar(self):
        if not ((searchLogin(self.ui.emailLineEdit.text(), self.ui.passwordLineEdit.text()))):
            self.ui.labelErrorLogin.setText('Erro ao logar')
        else:
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.bemvindoLabel.setText("Bem Vindo, "+getUsername(self.ui.emailLineEdit.text())[0][0]+"!") #! alterar para o username do banco
            self.userChat(self.ui.emailLineEdit.text())

    def timer_timeout(self):
        # Stop the timer
        self.timer.stop()

    def changePageToCadastro(self):
        
        self.timer.start(1000)  # 1 second delay
        self.ui.stackedWidget.setCurrentIndex(1)

    def changePageToLogar(self):
        
        self.timer.start(1000)  # 1 second delay
        self.ui.stackedWidget.setCurrentIndex(0)

    def cadastro(self):
        # Activate the second page of the stacked widget
        self.ui.stackedWidget.setCurrentIndex(1)
        username = self.ui.nameCadastrarLineEdit.text()
        email = self.ui.emailCadastrarLineEdit.text()
        password = self.ui.senhaCadastrarLineEdit.text()
        if(self.ui.confSenhaCadastrarLineEdit.text() == self.ui.senhaCadastrarLineEdit.text() ):
            result = registerUser(username, email, password)
            if not result:
                self.ui.labelErrorCadastrar.setText('Usuário já existe.')
            else:
                self.ui.labelErrorCadastrar.setText('Usuário cadastrado com sucesso!')
                self.ui.stackedWidget.setCurrentIndex(0)
        else:
                self.ui.labelErrorCadastrar.setText('Senhas Diferentes.')

    
    def userChat(self,email):
        chat = viewChat(email)
        if(len(chat)):
            user = chat[:,0]
            GPT = chat[:,1]
            for i in range(0,len(GPT)):
                
                
                newUser = userWidget(self.ui.widgetChatArea)
                self.ui.verticalLayout_2.addWidget(newUser)
                newUser.labelTextUser.setText(user[i])

                newUser2 = AIWidget('',self.ui.widgetChatArea)
                self.ui.verticalLayout_2.addWidget(newUser2)
                newUser2.labelTextAI.setText(GPT[i])


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())