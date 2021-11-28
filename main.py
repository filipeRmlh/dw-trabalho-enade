# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sqlite3

from database.load_data_into_base import connect_and_load
from dictionaries.paths_dict import database_root_path


def start_connection():
    print('Starting connection')
    return sqlite3.connect(database_root_path)


def end_connection(connection):
    print('Closing connection')
    connection.close()


if __name__ == '__main__':
    connection = start_connection()
    end_connection(connection)
