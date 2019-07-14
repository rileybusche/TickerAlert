import requests
import json

# Posts to Discord
def postToDiscord(message):
    
    hook_url = open("hook_url.txt", "r").read()
    params = {
        "content" : message,
        "username" : "Ticker Alert"
    }

    post = requests.post(hook_url, params)    

    print(post)

# Make API Call
def callAPI(ticker):
    response = requests.get(f'https://api.cryptonator.com/api/ticker/{ticker.lower()}-usd')
    response_json = response.json()
    print(response)
    print(response_json)


    # Posts if succesful 
    if response.status_code == 200:
        price = float(response_json["ticker"]["price"])

        print(price)
        #postToDiscord("BTC: ${}".format(price))
        result = f"The Price of {ticker} is: ${price:.2f}"

    else:
        #postToDiscord("Response code not 200: {}".format(response.status_code))
        result = f"Response code not 200: {response.status_code}"
    
    return result





