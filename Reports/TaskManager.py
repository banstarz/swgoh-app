from .DatabaseManager import DatabaseManager
from .ReportBuildersManager import ReportBuildersManager
import datetime

class TaskManager:
    
    def __init__(self, report_name, cred = []):
        self.rb_manager = ReportBuildersManager(report_name, cred)
        self.db_manager = DatabaseManager(report_name, 
                                            self.rb_manager.get_api_name(), 
                                            self.rb_manager.report_structure())
        self.date_format = '%Y-%m-%d %H:%M:%S'
        self.refresh_access_token_if_needed()

    def refresh_access_token_if_needed(self):
        token_expiration_date = self.db_manager.get_access_token_expiration_date() or '1970-01-01 00:00:00'
        token_expiration_date = datetime.datetime.strptime(token_expiration_date, self.date_format)
        datetime_now = datetime.datetime.now()
        if token_expiration_date < datetime_now:
            api_name = self.rb_manager.get_api_name()
            access_token, expires_in = self.rb_manager.refresh_access_token()
            new_expiration_date = datetime_now + datetime.timedelta(seconds=expires_in)
            new_expiration_date = datetime.datetime.strftime(new_expiration_date, self.date_format)
            self.db_manager.update_access_token(api_name, access_token, new_expiration_date)

    def refresh_data_if_needed(self, allycode=0):
        table_max_date = self.db_manager.get_max_date() or '1970-01-01 00:00:00'
        datetime_last =  datetime.datetime.strptime(table_max_date, self.date_format) 
        datetime_now = datetime.datetime.now()
        if (datetime_now - datetime_last).total_seconds() > 14400:
            access_token = self.db_manager.get_access_token()
            flattened_data_iterator = self.rb_manager.get_flattened_data_iterator()
            self.db_manager.refresh_data(flattened_data_iterator(allycode, access_token), self.rb_manager.report_structure())

    def get_records(self, allycode=0):
        self.refresh_data_if_needed(allycode)
        return self.db_manager.get_records()

    def get_field_names(self):
        return self.db_manager.report_builder.fields()