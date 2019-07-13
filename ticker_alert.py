import requests
import json

# Posts to Discord
def postToDiscord(message):
    
    hook_url = ''
    params = {
        "content" : message,
        "username" : "Ticker Alert"
    }

    post = requests.post(hook_url, params)    

    print(post)

# Make API Call
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    response_json = response.json()
except:
    print("Could not make API request")

# Posts if succesful 
if response.status_code == 200:
    price = response_json["bpi"]["USD"]["rate"]

    print(price)
    postToDiscord("BTC: ${}".format(price))
else:
    postToDiscord("Response code not 200: {}".format(response.status_code))




