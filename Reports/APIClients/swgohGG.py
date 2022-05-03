import requests
import json

class SwgohGGApiClient:
    
    BASE_URL = r'http://swgoh.gg/api/'
    CHARACTERS = r'characters/'
    SHIPS = r'ships/'
    api_name = 'swgoh_gg_api'

    def auth(self):
        return ('Fake_access_token', 100000000)

    @classmethod
    def swgoh_characters(cls):
        with requests.post(cls.BASE_URL+cls.CHARACTERS) as response:
            if response.status_code == 200:
                return response.json()
            else:
                return None

    @classmethod       
    def swgoh_ships(cls):
        with requests.post(cls.BASE_URL+cls.SHIPS) as response:
            if response.status_code == 200:
                return response.json()
            else:
                return None