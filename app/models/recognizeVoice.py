import io
import os

from google.cloud import speech_v1p1beta1 as speech


def convertAudioToText(audio):
    """
    @Transcribes the audio data using Google Cloud Speech-to-Text API.

    Args:
        audio (bytes): The audio data to transcribe, as a byte string.

    Returns:
        The first result of the transcrition

    Raises:
        google.api_core.exceptions.GoogleAPIError: If the request fails.
    """
    
    # Instantiates a client
    client = speech.SpeechClient()

    # Loads the audio data into memory
    audio = speech.RecognitionAudio(content=audio_data)

    # Configure the speech recognition request
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')

    # Detects speech in the audio data
    response = client.recognize(config=config, audio=audio)

    return 'Transcription: {}'.format(response.results[0].alternatives[0].transcript)
