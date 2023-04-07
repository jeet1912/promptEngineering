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

def getCryptoPrices():

    # define api endpoint and query params
    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"
    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"7d"}

    # define request headers with api key and host
    headers = {
        "X-RapidAPI-Key": "7f4d53cc47msh214301e0e9baec0p1694ddjsna8c84cadc4fa",
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }

    # send a get request to API endpoint with query params and headers
    response = requests.request("GET", url, headers=headers, params=querystring)

    # parse response as a JSON object
    JSONResult = json.load(response.text)

    history = JSONResult["data"]["history"]
    prices = []

    for value in history:
        prices.append(value["price"])
    
    priceList = ','.join(prices)
    
    return priceList

