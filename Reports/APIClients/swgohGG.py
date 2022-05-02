import requests
import json

class SwgohGGApiClient:
    
    def __init__(self, *args):
        self.BASE_URL = r'http://swgoh.gg/api/'
        self.CHARACTERS = r'characters/'
        self.api_name = 'swgoh_gg_api'

    def auth(self):
        return ('Fake_access_token', 100000000)

    def swgoh_characters(self):
        with requests.post('http://swgoh.gg/api/characters') as response:
            if response.status_code == 200:
                return response.json()
            else:
                return None

    def swgoh_ships(self):
        with requests.post('http://swgoh.gg/api/ships') as response:
            if response.status_code == 200:
                return response.json()
            else:
                return None