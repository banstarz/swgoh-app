import sqlite3


class SqlQueries():

    def select_data_query(tablename):
        SELECT_DATA_QUERY = f'''
            SELECT * FROM {tablename}
        '''
        return SELECT_DATA_QUERY

    def drop_table_query(tablename):
        DROP_TABLE_QUERY = f'''
            DELETE FROM {tablename}
        '''
        return DROP_TABLE_QUERY

    def get_max_date_query(tablename):
        GET_MAX_DATE_QUERY = f'''
            SELECT max(datetime) FROM {tablename}
        '''
        return GET_MAX_DATE_QUERY

    def insert_query(self, tablename, report_structure):
        INSERT_INTO_QUERY = f'''
            INSERT INTO {tablename} VALUES
        '''
        fields_count = len(report_structure.keys())
        question_marks = ','.join(['?' for _ in range(fields_count)])
        return INSERT_INTO_QUERY + f' ({question_marks})'

    def create_access_tokens_if_not_exists_query():
        CREATE_ACCESS_TOKENS_IF_NOT_EXISTS_QUERY = '''
            CREATE TABLE IF NOT EXISTS access_tokens
            (api_name varchar(255),
            access_token varchar(255),
            expiration_date date)
        '''
        return CREATE_ACCESS_TOKENS_IF_NOT_EXISTS_QUERY

    def get_token_expiration_date_query(tablename, api_name):
        GET_TOKEN_EXPIRATION_DATE_QUERY = f'''
            SELECT expiration_date FROM access_tokens
            WHERE api_name = "{api_name}"
        '''
        return GET_TOKEN_EXPIRATION_DATE_QUERY

    def delete_expired_token_query(api_name):
        DELETE_EXPIRED_TOKEN_QUERY = f'''
            DELETE from access_tokens
            where api_name = "{api_name}"
        '''
        return DELETE_EXPIRED_TOKEN_QUERY

    def update_access_token(self, api_name, access_token, expiration_date):
        INSERT_OR_UPDATE_TOKEN_QUERY = f'''
            INSERT into access_tokens VALUES
            ("{api_name}", "{access_token}", "{expiration_date}")
        '''
        return INSERT_OR_UPDATE_TOKEN_QUERY

    def get_access_token_query(tablename, api_name):
        GET_ACCESS_TOKEN_QUERY = f'''
            SELECT access_token from access_tokens
            WHERE api_name = "{api_name}"
        '''
        return GET_ACCESS_TOKEN_QUERY

    def get_table_by_name_query(tablename):
        GET_TABLE_BY_NAME_QUERY = f'''
            SELECT *
            FROM sqlite_schema
            WHERE name = "{tablename}"
        '''
        return GET_TABLE_BY_NAME_QUERY

    def create_table_query(self, tablename, report_structure):
        CREATE_IF_NOT_EXISTS_QUERY = f'''
            CREATE TABLE IF NOT EXISTS {tablename}
        '''
        fields_list = [f'{field} {fieldtype}' for field, fieldtype in report_structure.items()]
        fields = ', '.join(fields_list)
        return CREATE_IF_NOT_EXISTS_QUERY + f' ({fields})'