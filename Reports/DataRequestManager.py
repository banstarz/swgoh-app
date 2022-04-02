from .DatabaseManager import DatabaseManager
import datetime

class DataRequestManager:
    def __init__(self, report_name, cred = []):
        self.db_manager = DatabaseManager(report_name, cred)

    def refresh_data_if_needed(self, allycode=0):
        date_format = '%Y-%m-%d %H:%M:%S'
        table_max_date = self.db_manager.get_max_date() or '1970-01-01 00:00:00'
        datetime_last =  datetime.datetime.strptime(table_max_date, date_format) 
        datetime_now = datetime.datetime.now()
        if (datetime_now - datetime_last).total_seconds() > 14400:
            self.db_manager.refresh_data(allycode)

    def get_records(self, allycode=0):
        self.refresh_data_if_needed(allycode)
        return self.db_manager.get_records()

    def get_field_names(self):
        return self.db_manager.report_builder.fields()