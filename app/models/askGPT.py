import openai
import json
from askWatson import callWatson

# Load the JSON file
with open('C:/credentials/credentials.json', 'r') as f:
    keys = json.load(f)

# Set up the OpenAI API key
openai.api_key = keys['chatGPT']

# Initialize the conversation history as an empty list
#!history = []

def generateResponse():
    
    # Load the JSON file
    with open('/app/ultis/transcriptions.json', 'r') as f:
        transcriptions = json.load(f)

    # Add the current question to the conversation history
    history.append({"role": "user", "content": transcriptions['text']})
    
    # Concatenate all previous questions and responses
    prompt = history
    
    # Generate the response using the OpenAI API
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=prompt,
      max_tokens=64,
      n=1,
      stop=[" Human:", " AI:"],
      temperature=0.6,
    )
    
    # Add the current response to the conversation history
    response_text = response.choices[0]['text'].strip()
    #!history.append({"role": "assistant", "content": response_text})

    # Convert the transcribed text to a list of JSON objects
    results = []

    for result in response.choices:  #! not certain
        result_dict = {
            'text': result['text']
        }
        results.append(result_dict)

    # Save the transcribed text as a JSON file
    with open('/app/ultis/responses.json', 'w') as f:
        json.dump(results, f)

    
    # Return the API-generated response
    
    return callWatson(response_text)
