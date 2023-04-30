import io
import os
import json

from app.models.askGPT import generateResponse

from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account

import librosa
import soundfile as sf


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'app\credentials\credentials.json'

def convertAudioToText():
    """
    Transcribes the given audio data using Google Cloud Speech-to-Text API,
    and saves the transcribed text to a JSON file.

    Args:
        @audio (bytes): The audio data to transcribe, as a byte string.

    Returns:
        None

    Raises:
        google.api_core.exceptions.GoogleAPIError: If the request fails.
    """
    key_path = r'app\credentials\credentials.json'

    # Create credentials object from the key file
    credentials = service_account.Credentials.from_service_account_file(key_path)

    # Create a SpeechClient object with the credentials
    client = speech.SpeechClient(credentials=credentials)
        
    # Load the audio file
    audio, sr = librosa.load(r'app\utils\recorded_audio.wav', sr=48000)

    # Resample the audio to 16000 Hz
    resampled_audio = librosa.resample(audio,orig_sr=sr, target_sr=16000)

    # Save the resampled audio to a file
    sf.write(r'app\utils\recorded_audio2.wav', resampled_audio, 16000)

    
    # Instantiates a client
    client = speech.SpeechClient()
    
    wav_bytes = ''
    # Loads the audio data into memory
    with open(r'app\utils\recorded_audio2.wav', 'rb') as f:
        wav_bytes = f.read()
    audio = speech.RecognitionAudio(content=wav_bytes)
    
    # Configure the speech recognition request
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')

    
    # Detects speech in the audio data
    response = client.recognize(config=config, audio=audio)


    # Convert the transcribed text to a list of JSON objects
    results = []
    print(response.results)
        
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))
        results.append("Transcript: {}".format(result.alternatives[0].transcript))
    
    # Save the transcribed text as a JSON file
    with open('app/utils/transcriptions.json', 'w') as f:
        json.dump(results, f)

    generateResponse()
    