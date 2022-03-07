import requests
import json

class Requester:
    def __init__(self):
        self.BASE_URL = r'https://api.swgoh.help/'
        self.AUTH = r'auth/signin'
        self.GUILD = r'swgoh/guilds'
        self.UNITS = r'swgoh/units'

    def auth(self):
        req_body = {
            'username': 'alstraze',
            'password': 'EFeFiYDSB!3i!Nh',
            'grant_type': 'password',
            'client_id': 'alstraze',
            'client_secret': 'EFeFiYDSB'
        }
        with requests.post(self.BASE_URL+self.AUTH, data=req_body) as response:
            return response.json()['access_token']


    def guild_info(self, allycode):
        access_token = self.auth()

        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }

        req_body = {
            'allycodes': allycode,
        }
        with requests.post(self.BASE_URL+self.GUILD, headers=headers, data=req_body) as response:
            response = json.dumps(response.json(), indent=4, ensure_ascii=False)

        return json.loads(response)[0]['roster']