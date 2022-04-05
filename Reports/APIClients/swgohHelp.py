import requests

class SwgohHelpApiClient:
    
    def __init__(self, cred):
        self.BASE_URL = r'https://api.swgoh.help/'
        self.AUTH = r'auth/signin'
        self.GUILD = r'swgoh/guilds'
        self.UNITS = r'swgoh/units'
        self.PLAYERS = r'swgoh/players'
        self.ROSTER = r'swgoh/roster'
        self.cred = cred
        self.api_name = 'swgoh_help_api'

    def auth(self):
        req_body = {
            'username': self.cred['username'],
            'password': self.cred['password'],
            'grant_type': 'password',
            'client_id': self.cred['username'],
            'client_secret': self.cred['client_secret']
        }

        with requests.post(self.BASE_URL+self.AUTH, data=req_body) as response:
            resp = response.json()
            return (resp['access_token'], int(resp['expires_in']))

    def guild(self, allycode, access_token):
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        req_body = {
            'allycodes': allycode,
        }

        with requests.post(self.BASE_URL+self.GUILD, headers = headers, data=req_body) as response:
            return response.json()
        
    def players(self, allycode, access_token):
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        req_body = {
            'allycodes': allycode,
        }

        with requests.post(self.BASE_URL+self.PLAYERS, headers = headers, data=req_body) as response:
            return response.json()