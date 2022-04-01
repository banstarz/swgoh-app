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
        self.DROP_TABLE_QUERY = f'''
        DELETE FROM {self.tablename}
        '''
    
    @staticmethod
    def query_result_generator(cursor):
        res = [desc[0] for desc in cursor.description]
        while res:
            yield res
            res = cursor.fetchone()

    @staticmethod
    def execute_sql_query(sql_query, need_sql_result=False):
        with sqlite3.connect('swgoh.db') as conn:
            cur = conn.cursor()
            cur.execute(sql_query)
            conn.commit()
            if need_sql_result:
                return DatabaseManager.query_result_generator(cur)

    def _generate_insert_query(self):
        fields_count = len(self.report_builder.FIELDS.keys())
        question_marks = ','.join(['?' for _ in range(fields_count)])
        return self.INSERT_INTO_QUERY + f' ({question_marks})'

    def _generate_create_table_query(self):
        fields_list = [f'{field} {fieldtype}' for field, fieldtype in self.report_builder.report_structure().items()]
        fields = ', '.join(fields_list)
        return self.CREATE_IF_NOT_EXISTS_QUERY + f' ({fields})'        

    def create_table_if_not_exists(self):
        sql_query = self._generate_create_table_query()
        DatabaseManager.execute_sql_query(sql_query)
    
    def drop_table(self):
        DatabaseManager.execute_sql_query(self.DROP_TABLE_QUERY)

    def get_max_date(self):
        self.create_table_if_not_exists()
        res = DatabaseManager.execute_sql_query(self.GET_MAX_DATE_QUERY, need_sql_result=True)
        next(res)
        return next(res)[0]

    def refresh_data(self, allycode):
        if not self.report_builder.IS_INCREMENTAL:
            self.drop_table()
        flattened_data_iterator = self.report_builder.get_record
        with sqlite3.connect('swgoh.db') as conn:
            cur = conn.cursor()
            cur.executemany(self._generate_insert_query(), flattened_data_iterator(allycode))

    def get_records(self):
        yield from DatabaseManager.execute_sql_query(self.SELECT_DATA_QUERY, need_sql_result=True)

    @staticmethod
    def get_all_tables_names():
        GET_TABLES_NAMES_QUERY = "SELECT name as \'Tables names\' FROM sqlite_master WHERE type='table'"
        yield from DatabaseManager.execute_sql_query(GET_TABLES_NAMES_QUERY, need_sql_result=True)