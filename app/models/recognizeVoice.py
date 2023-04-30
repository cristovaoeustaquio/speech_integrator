import io
import os
import json

from google.cloud import speech_v1p1beta1 as speech


def convertAudioToText(audio):
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


    # Convert the transcribed text to a list of JSON objects
    results = []
    for result in response.results:
        text = result.alternatives[0].transcript
        start_time = result.alternatives[0].words[0].start_time.seconds + \
                     result.alternatives[0].words[0].start_time.nanos / 1e9
        end_time = result.alternatives[0].words[-1].end_time.seconds + \
                   result.alternatives[0].words[-1].end_time.nanos / 1e9
        result_dict = {
            'text': text,
            'start_time': start_time,
            'end_time': end_time
        }
        results.append(result_dict)

    # Save the transcribed text as a JSON file
    with open('/app/ultis/response.json', 'w') as f:
        json.dump(results, f)
    