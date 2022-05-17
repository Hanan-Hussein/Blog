import urllib3
import json
from datetime import datetime

Random_Quote_Url='http://quotes.stormconsultancy.co.uk/random.json'

def get_random_quote():
    http = urllib3.PoolManager()
    response = http.request('GET', Random_Quote_Url)
    news_response = json.loads(response.data.decode('utf-8'))

    return news_response
    
