import requests
import json


fmp_URL = 'https://financialmodelingprep.com/api/v3/company/profile/%s'

'''
Now that we imported the required libraries , we define the function. This works through data taken from the fmp_URL link and it returns the name of the company selected and its stock price. 
'''
def get_price(company="AAPL"):             
    r = requests.get(fmp_URL % company)
    data = json.loads(r.text)
    price = data['profile']['price']
    name = data['profile']['companyName']
    return price, name
