import sqlite3

from .SqlQueries import SqlQueries


class DatabaseManager():
    
    @staticmethod
    def query_result_generator(cursor):
        res = [desc[0] for desc in cursor.description]
        while res:
            yield res
            res = cursor.fetchone()

    @staticmethod
    def execute_sql_query(sql_query, need_only_last=False, need_sql_result=False):
        with sqlite3.connect('swgoh.db') as conn:
            cur = conn.cursor()
            cur.execute(sql_query)
            conn.commit()
            if need_only_last:
                count = 0
                for last in DatabaseManager.query_result_generator(cur):
                    count += 1
                if count == 1:
                    return None
                else:
                    return last[0]

            if need_sql_result:
                return DatabaseManager.query_result_generator(cur)

    @staticmethod
    def get_all_tables_names():
        GET_TABLES_NAMES_QUERY = SqlQueries.get_tables_names_query()
        yield from DatabaseManager.execute_sql_query(GET_TABLES_NAMES_QUERY, need_sql_result=True)

    def create_access_tokens_if_not_exists(self):
        sql_query = SqlQueries.create_access_tokens_if_not_exists_query()
        DatabaseManager.execute_sql_query(sql_query, need_sql_result=False)

    def create_table_if_not_exists(self, tablename, report_structure):
        sql_query = SqlQueries.create_table_query(tablename, report_structure)
        DatabaseManager.execute_sql_query(sql_query, need_sql_result=False)

    def drop_table(self, tablename):
        sql_query = SqlQueries.drop_table_query(tablename)
        DatabaseManager.execute_sql_query(sql_query, need_sql_result=False)

    def get_access_token_expiration_date(self, apiname):
        sql_query = SqlQueries.get_token_expiration_date_query(apiname)
        return DatabaseManager.execute_sql_query(sql_query, need_only_last=True)

    def update_access_token(self, api_name, access_token, expiration_date):
        sql_query = SqlQueries.delete_expired_token_query(api_name)
        DatabaseManager.execute_sql_query(sql_query, need_sql_result=False)
        sql_query = SqlQueries.update_access_token(api_name, access_token, expiration_date)
        DatabaseManager.execute_sql_query(sql_query, need_sql_result=False)

    def get_access_token(self, api_name):
        sql_query = SqlQueries.get_access_token_query(api_name)
        return DatabaseManager.execute_sql_query(sql_query, need_only_last=True)

    def get_max_date(self, tablename):
        sql_query = SqlQueries.get_max_date_query(tablename)
        return DatabaseManager.execute_sql_query(sql_query, need_only_last=True)

    def refresh_data(self, tablename, report_structure, flattened_data_iterator, overwrite = False):
        if overwrite:
            self.drop_table(tablename)
        with sqlite3.connect('swgoh.db') as conn:
            cur = conn.cursor()
            cur.executemany(SqlQueries.insert_query(tablename, report_structure), flattened_data_iterator)

    def get_records(self, tablename):
        sql_query = SqlQueries.get_records_query(tablename)
        return DatabaseManager.execute_sql_query(sql_query, need_sql_result=True)