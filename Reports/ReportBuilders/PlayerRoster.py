import datetime
from ..APIClients.swgohHelp import SwgohHelpApiClient
from ..BaseClasses import ReportBuilder


class PlayerRosterReportBuilder(ReportBuilder):
    
    def __init__(self, cred):
        self.client = SwgohHelpApiClient(cred)
        self.api_response = []
        self.FIELDS = {
            'allycode': 'int',
            'player': 'varchar(255)',
            'character': 'varchar(255)',
            'level': 'int',
            'gp': 'int',
            'star': 'int',
            'gear': 'int',
            'relic': 'int',
            'zetas': 'int',
            'datetime': 'date'
        }
        self.TABLE_NAME = 'player_roster'
        self.IS_INCREMENTAL = False
        
    def _extract_data(self, allycode, access_token):
        self.api_response = self.client.players(allycode, access_token)
        
    def __zetas(self, character):
        return sum([flag['isZeta'] for flag in character['skills'] if flag['tier'] >= 8])

    def __relic(self, character):
        relic = character['relic']
        if relic:
            return relic['currentTier'] if relic['currentTier'] > 1 else "NULL"
        else:
            return "NULL"

    def fields(self):
        return self.FIELDS.keys()

    def report_structure(self):
        return self.FIELDS

    def _flatten_report(self):
        today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        allycode = self.api_response[0]['allyCode']
        name = self.api_response[0]['name']
        for char in self.api_response[0]['roster']:
            yield (allycode,
                    name,
                    char['defId'],
                    char['level'],
                    char['gp'],
                    char['rarity'],
                    char['gear'],
                    self.__relic(char),
                    self.__zetas(char),
                    today
                )

    def get_record(self, allycode, access_token):
        self._extract_data(allycode, access_token)
        for record in self._flatten_report():
            yield record