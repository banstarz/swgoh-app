import datetime
from ..APIClients.swgohGG import SwgohGGApiClient
from ..BaseClasses import ReportBuilder


class SwgohShipsReportBuilder(ReportBuilder):
    
    def __init__(self, *args):
        self.client = SwgohGGApiClient()
        self.FIELDS = {
            'game_name': 'varchar(255)',
            'base_name': 'varchar(255)',
            'datetime': 'date'
        }
        self.TABLE_NAME = 'swgoh_ships'
        self.IS_INCREMENTAL = False
        
    def _extract_data(self):
        self.api_response = self.client.swgoh_ships()

    def fields(self):
        return self.FIELDS.keys()

    def report_structure(self):
        return self.FIELDS

    def _flatten_report(self):
        if self.api_response is None:
            return None
        today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        for unit in self.api_response:
            yield (unit['name'],
                    unit['base_id'],
                    today
                )

    def get_record(self, *args):
        self._extract_data()
        for record in self._flatten_report():
            yield record