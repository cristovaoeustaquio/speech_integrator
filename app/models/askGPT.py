import openai
import json
from app.models.askWatson import callWatson

# Load the JSON file
with open('C:/credentials/credentials.json', 'r') as f:
    keys = json.load(f)

# Set up the OpenAI API key
openai.api_key = keys['chatGPT']

# Initialize the conversation history as an empty list
history = []

def generateResponse():
    
    # Load the JSON file
    with open('app/utils/transcriptions.json', 'r') as f:
        transcriptions = json.load(f)

    # Add the current question to the conversation history
    #history.append({"role": "user", "content": transcriptions['text']})
    
    # Concatenate all previous questions and responses
    prompt = transcriptions[0][10::]

    print('teste',prompt)
    
    # Generate the response using the OpenAI API
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role":"user","content":prompt}]
    )
    
    print('teste',response)
    print('teste',response.choices[0])
    print('teste',response.choices[0]['message']['content'])
    # Add the current response to the conversation history
    response_text = response.choices[0]['message']['content']
    #!history.append({"role": "assistant", "content": response_text})

    # Convert the transcribed text to a list of JSON objects
    results = []

    for result in response.choices:  #! not certain
        result_dict = {
            'text': result['message']['content']
        }
        results.append(result_dict)

    # Save the transcribed text as a JSON file
    with open('app/utils/responses.json', 'w') as f:
        json.dump(results, f)

    
    # Return the API-generated response
    
    return callWatson(response_text)
