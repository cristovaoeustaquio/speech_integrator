import os
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

# Load the JSON file
with open('c:\credentials/credentials.json', 'r') as f:
    keys = json.load(f)

# Set up the Watson API key
api_key = keys['IBM']

def callWatson(user,chat):
    # Configuração da autenticação com o serviço
    authenticator = IAMAuthenticator(api_key)
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )
    text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/bd7910a4-f9e0-4685-84c5-721896022527')

    # Texto que será convertido em fala
    texto = chat
    # Obtém a lista de vozes disponíveis
    #voices = text_to_speech.list_voices().get_result()
    #print("Voices: \n{}".format(voices))
    #pt-BR_IsabelaV3Voice 
    #en-US_AllisonExpressive

    # Configuração da saída de áudio
    audio_file = open('outputAI.wav', 'wb')
    
    audio_file.write(
        text_to_speech.synthesize(
            texto,
            voice='pt-BR_IsabelaV3Voice',
            accept='audio/wav'
        ).get_result().content)
    
    audio_file.close()
        

    return(user,chat,'outputAI.wav')  