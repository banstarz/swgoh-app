import datetime
from .APIClients.swgohGG import SwgohGGApiClient
from .BaseClasses import ReportBuilder


class SwgohUnitsReportBuilder(ReportBuilder):
    def __init__(self, *args):
        self.client = SwgohGGApiClient()
        self.FIELDS = {
            'player': 'varchar(255)',
            'character': 'varchar(255)',
            'datetime': 'date'
        }
        self.TABLE_NAME = 'swgoh_units'
        self.IS_INCREMENTAL = False
        
        
    def _extract_data(self):
        self.api_response = self.client.swgoh_units()

    def fields(self):
        return self.FIELDS.keys()

    def report_structure(self):
        return self.FIELDS

    def _flatten_report(self):
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