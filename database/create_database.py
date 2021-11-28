import sqlite3
from dictionaries.paths_dict import *


def get_sql_schema_creation_file_content(file_path):
    f = open(file_path, "r")
    return str(f.read())


def create_schema(conn, schema_sql_file):
    print('Migrating database ddl')
    content = get_sql_schema_creation_file_content(schema_sql_file)
    conn.executescript(content)
    print('Database schema creation finished')


if __name__ == '__main__':
    print('Starting connection')
    connection = sqlite3.connect(database_root_path)
    create_schema(connection, 'database_schema.sql')
    print('Closing connection')
    connection.close()

