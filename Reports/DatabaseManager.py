import sqlite3


class DatabaseManager():
    
    def __init__(self, tablename, api_name, report_structure):
        self.tablename = tablename
        self.api_name = api_name
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
        self.CREATE_ACCESS_TOKENS_IF_NOT_EXISTS_QUERY = '''
        CREATE TABLE IF NOT EXISTS access_tokens
        (api_name varchar(255),
        access_token varchar(255),
        expiration_date date)
        '''
        self.GET_TOKEN_EXPIRATION_DATE_QUERY = f'''
        SELECT expiration_date FROM access_tokens
        WHERE api_name = "{self.api_name}"
        '''
        self.GET_ACCESS_TOKEN = f'''
        SELECT access_token from access_tokens
        WHERE api_name = \"{self.api_name}\"
        '''
        self._create_access_tokens_if_not_exists()
        self._create_table_if_not_exists(report_structure)

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

    @staticmethod
    def get_all_tables_names():
        GET_TABLES_NAMES_QUERY = "SELECT name as \'Tables names\' FROM sqlite_master WHERE type='table'"
        yield from DatabaseManager.execute_sql_query(GET_TABLES_NAMES_QUERY, need_sql_result=True)

    def _generate_insert_query(self, report_structure):
        fields_count = len(report_structure.keys())
        question_marks = ','.join(['?' for _ in range(fields_count)])
        return self.INSERT_INTO_QUERY + f' ({question_marks})'

    def _generate_create_table_query(self, report_structure):
        fields_list = [f'{field} {fieldtype}' for field, fieldtype in report_structure.items()]
        fields = ', '.join(fields_list)
        return self.CREATE_IF_NOT_EXISTS_QUERY + f' ({fields})'

    def _create_access_tokens_if_not_exists(self):
        DatabaseManager.execute_sql_query(self.CREATE_ACCESS_TOKENS_IF_NOT_EXISTS_QUERY)

    def _create_table_if_not_exists(self, report_structure):
        sql_query = self._generate_create_table_query(report_structure)
        DatabaseManager.execute_sql_query(sql_query)
    
    def _drop_table(self):
        DatabaseManager.execute_sql_query(self.DROP_TABLE_QUERY)

    def get_access_token_expiration_date(self):
        expiration_date_query_result = DatabaseManager.execute_sql_query(self.GET_TOKEN_EXPIRATION_DATE_QUERY, need_sql_result=True)
        expiration_date = list(expiration_date_query_result)
        return list(expiration_date)[-1][0] if len(expiration_date) > 1 else None

    def update_access_token(self, api_name, access_token, expiration_date):
        DELETE_EXPIRED_TOKEN_QUERY = '''
        DELETE from access_tokens
        where api_name = "{api_name}";
        '''
        DatabaseManager.execute_sql_query(DELETE_EXPIRED_TOKEN_QUERY)
        INSERT_OR_UPDATE_TOKEN_QUERY = f'''
        INSERT or REPLACE into access_tokens VALUES
        ("{api_name}", "{access_token}", "{expiration_date}");
        '''
        DatabaseManager.execute_sql_query(INSERT_OR_UPDATE_TOKEN_QUERY)

    def get_access_token(self):
        access_token_query_result = DatabaseManager.execute_sql_query(self.GET_ACCESS_TOKEN, need_sql_result=True)
        access_token = list(access_token_query_result)
        return access_token[-1][0] if len(access_token) > 1 else None

    def get_max_date(self):
        res = DatabaseManager.execute_sql_query(self.GET_MAX_DATE_QUERY, need_sql_result=True)
        next(res)
        return next(res)[0]

    def refresh_data(self, flattened_data_iterator, report_structure, overwrite = False):
        if overwrite:
            self._drop_table()
        with sqlite3.connect('swgoh.db') as conn:
            cur = conn.cursor()
            cur.executemany(self._generate_insert_query(report_structure), flattened_data_iterator)

    def get_records(self):
        yield from DatabaseManager.execute_sql_query(self.SELECT_DATA_QUERY, need_sql_result=True)