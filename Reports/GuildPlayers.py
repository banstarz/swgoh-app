import datetime
from .APIClients.swgohHelp import SwgohHelpApiClient
from .BaseClasses import ReportBuilder


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
        
        
    def _extract_data(self, allycode):
        self.api_response = self.client.guild(allycode)
    

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

    def get_record(self, allycode):
        self._extract_data(allycode)
        for record in self._flatten_report():
            yield record