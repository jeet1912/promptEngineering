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

def GetCryptoPrices():

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
    JSONResult = json.loads(response.text)

    history = JSONResult["data"]["history"]
    prices = []

    for value in history:
        prices.append(value["price"])
    
    priceList = ','.join(prices)
    
    return priceList

bitcoinPrices = GetCryptoPrices()

chatGPTPrompt = f"""I will provide you with a list of bitcoin prices for the last seven days. Could you provide me with a technical analysis of Bitcoin based on these prices. Here is what I want:
Price Overview,
Moving Averages,
Relative Strength Index (RSI),
Moving Average Convergence Divergence (MACD),
Advice and Suggestion,
Do I buy or sell?
Please be as detailed, and explain in a way any beginner can understand.
Here is the price list: {bitcoinPrices}
"""

analysis = BasicGeneration(chatGPTPrompt)

print(analysis)