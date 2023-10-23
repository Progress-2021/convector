import requests

URL = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_wJAS9ZardqiaCKSXI0jq2NsuPIpoL86KnGLBqaNj' # &currencies=
API_KEY = 'fca_live_wJAS9ZardqiaCKSXI0jq2NsuPIpoL86KnGLBqaNj'

def get_currencies():
    response = requests.get(URL)
    return response.json()

