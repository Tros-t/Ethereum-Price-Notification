# Imports 

import requests 
from pushbullet import Pushbullet 

# Pushbullet token
pb = Pushbullet("YOUR_PUSHBULLET_KEY")

# Url
url = "https://min-api.cryptocompare.com/data/price?fsym=Eth&tsyms=USD,AED"



# GET request 
res = requests.get(url)

# getting json
json = res.json()

# getting values
usd = str(json["USD"])
aed = str(json["AED"])

price_string = "AED: " + aed + "   USD: " + usd
# Pushing a note to android device (Can be IOS)
pb.push_note("Ethereum Price Now", price_string)


