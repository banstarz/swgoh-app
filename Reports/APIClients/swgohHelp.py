import requests

class SwgohHelpApiClient:

    BASE_URL = r'https://api.swgoh.help/'
    AUTH = r'auth/signin'
    GUILD = r'swgoh/guilds'
    UNITS = r'swgoh/units'
    PLAYERS = r'swgoh/players'
    ROSTER = r'swgoh/roster'
    api_name = 'swgoh_help_api'

    def __init__(self, cred):
        self.cred = cred

    def auth(self):
        req_body = {
            'username': self.cred['username'],
            'password': self.cred['password'],
            'grant_type': 'password',
            'client_id': self.cred['username'],
            'client_secret': self.cred['client_secret']
        }

        with requests.post(url=self.BASE_URL+self.AUTH, 
                            data=req_body) as response:
            resp = response.json()
            return (resp['access_token'], int(resp['expires_in']))

    @classmethod
    def guild(cls, allycode, access_token):
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        req_body = {
            'allycodes': allycode,
        }

        with requests.post(url=cls.BASE_URL+cls.GUILD, 
                            headers=headers, 
                            data=req_body) as response:
            return response.json()
        
    @classmethod
    def players(cls, allycode, access_token):
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        req_body = {
            'allycodes': allycode,
        }

        with requests.post(url=cls.BASE_URL+cls.PLAYERS, 
                            headers=headers, 
                            data=req_body) as response:
            return response.json()