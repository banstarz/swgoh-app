import datetime
from ..APIClients.swgohHelp import SwgohHelpApiClient
from ..BaseClasses import ReportBuilder


class GuildPlayersReportBuilder(ReportBuilder):
    
    def __init__(self, cred):
        self.client = SwgohHelpApiClient(cred)
        self.api_response = []
        self.FIELDS = {
            'guild_name': 'varvhar(255)',
            'name': 'varvhar(255)',
            'allyCode': 'int',
            'level': 'int',
            'gp': 'int',
            'gpChar': 'int',
            'gpShip': 'int',
            'datetime': 'date'
        }
        self.TABLE_NAME = 'guild_players'
        self.IS_INCREMENTAL = False
        
    def _extract_data(self, allycode, access_token):
        self.api_response = self.client.guild(allycode, access_token)

    def fields(self):
        return self.FIELDS.keys()

    def report_structure(self):
        return self.FIELDS

    def _flatten_report(self):
        today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        guild_name = self.api_response[0]["name"]
        for obj in self.api_response[0]['roster']:
            yield (guild_name,
                    obj["name"],
                    obj["allyCode"],
                    obj["level"],
                    obj["gp"],
                    obj["gpChar"],
                    obj["gpShip"],
                    today
                )

    def get_record(self, allycode, access_token):
        self._extract_data(allycode, access_token)
        for record in self._flatten_report():
            yield record