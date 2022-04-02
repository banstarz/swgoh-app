import requests
import json

class SwgohGGApiClient:
    def __init__(self, *args):
        self.BASE_URL = r'http://swgoh.gg/api/'
        self.CHARACTERS = r'characters/'

    def swgoh_units(self):
        with requests.post('http://swgoh.gg/api/characters') as response:
            return response.json()