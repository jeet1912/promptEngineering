import openai
import requests
import json

openai.api_key = "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"

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
        "role": "user",
        "content" : userPrompt
        }])
    return completion.choices[0].message.content
"""
prompt = "analyze last 7 days bitcoin prices"
response = BasicGeneration(prompt)
print(response)
"""

