import openai
import json
from models.askWatson import callWatson

# Load the JSON file
with open('C:\credentials/credentials.json', 'r') as f:
    keys = json.load(f)

# Set up the OpenAI API key
openai.api_key = keys['chatGPT']

def generateResponse(transcriptions):
    
    prompt = transcriptions

    
    # Generate the response using the OpenAI API
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role":"user","content":prompt}]
    )
    message = response.choices[0].message.content

    if len(message) > 50:
        idx = message.find(". ", 50)  # find the index of the first occurrence of ". " after 50 characters
        if idx != -1:  # if ". " is found after 50 characters
            message = message[:idx+2]  # 
    
    return callWatson(transcriptions,message)
