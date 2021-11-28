import sqlite3

from dictionaries.paths_dict import database_root_path


def learn():
    pass


def test():
    pass


def transform_columns():

def get_data(connection):
    query = "select * from"
    connection.execute()

def init(connection):
    get_data(connection)


if __name__ == '__main__':
    print('Starting connection')
    connection = sqlite3.connect(database_root_path)
    init(connection.cursor())
    print('Closing connection')
    connection.close()