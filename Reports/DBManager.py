import sqlite3
from .GuildPlayers import GuildPlayersReportBuilder
from .PlayerRoster import PlayerRosterReportBuilder

class DatabaseManager():
    
    def __init__(self, report_name, cred):
        self.BUILDER_BY_REPORT = {
            'guild_players': GuildPlayersReportBuilder,
            'player_roster': PlayerRosterReportBuilder
        }
        self.report_builder = self.BUILDER_BY_REPORT.get(report_name)(cred)
        self.tablename = self.report_builder.TABLE_NAME
        self.GET_MAX_DATE_QUERY = f'''
        SELECT max(datetime) FROM {self.tablename}
        '''
        self.INSERT_INTO_QUERY = f'''
        INSERT INTO {self.tablename} VALUES
        '''
        self.SELECT_DATA_QUERY = f'''
        SELECT * FROM {self.tablename}
        '''
        self.GET_TABLE_BY_NAME_QUERY = f'''
        SELECT *
        FROM sqlite_schema
        WHERE name = "{self.tablename}"
        '''
        self.CREATE_IF_NOT_EXISTS_QUERY = f'''
        CREATE TABLE IF NOT EXISTS {self.tablename}
        '''

    def _generate_insert_query(self):
        fields_count = len(self.report_builder.FIELDS.keys())
        question_marks = ','.join(['?' for _ in range(fields_count)])
        return self.INSERT_INTO_QUERY + f' ({question_marks})'

    def _generate_create_table_query(self):
        fields_list = [f'{field} {fieldtype}' for field, fieldtype in self.report_builder.report_structure().items()]
        fields = ','.join(fields_list)
        return self.CREATE_IF_NOT_EXISTS_QUERY + f' ({fields})'


    # def get_table_by_name(self):
    #     with sqlite3.connect('swgoh.db') as conn:
    #         conn.execute(self.GET_TABLE_BY_NAME_QUERY)
    #         return conn.fetchone()

    def create_table_if_not_exists(self):
        with sqlite3.connect('swgoh.db') as conn:
            cur = conn.cursor()
            cur.execute(self._generate_create_table_query())

    def get_max_date(self):
        self.create_table_if_not_exists()
        with sqlite3.connect('swgoh.db') as conn:
            cur = conn.cursor()
            cur.execute(self.GET_MAX_DATE_QUERY)
            return cur.fetchone()[0] or '1970-01-01 00:00:00'

    def refresh_data(self, allycode):
        flattened_data_iterator = self.report_builder.get_record
        with sqlite3.connect('swgoh.db') as conn:
            cur = conn.cursor()
            cur.executemany(self._generate_insert_query(), flattened_data_iterator(allycode))

    def get_records(self):
        with sqlite3.connect('swgoh.db') as conn:
            cur = conn.cursor()
            cur.execute(self.SELECT_DATA_QUERY)
            return cur.fetchall()