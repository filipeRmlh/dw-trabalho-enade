import sqlite3
from dictionaries.load_data_dict import dictionary_column_mapping
from database.treat_data import treat_data
from dictionaries.paths_dict import *


# The Function 'get_mapped_line' extracts values from csv line and return these values mapped to the following format
# {
#     <SQlTablename1> : {
#         "fields": [<sql_field1>, <sql_field2>, ...]
#         "values": [<sql_field1_corresponding_value>, <sql_field2_corresponding_value>, ...]
#     },
#     <SQlTablename2> : {
#         "fields": [<sql_field3>, <sql_field4>, ...]
#         "values": [<sql_field3_corresponding_value>, <sql_field4_corresponding_value>, ...]
#     }
#     ...
# }
def get_mapped_line(line, dictionary_year, first_line):
    mapped_line = {}
    for index in range(len(first_line)):
        if first_line[index] in dictionary_year:
            (table, field) = dictionary_year[first_line[index]]
            if table not in mapped_line:
                mapped_line[table] = {"fields": [], "values": []}
            treated_data = treat_data(table, field, line[index])
            # If has field with no valid information, ignore line.
            if treated_data == "N/A":
                return None
            mapped_line[table]["fields"].append(field)
            mapped_line[table]["values"].append(treated_data)
    return mapped_line


# Memoizing inserted dimensions values to not make a Select query.
memoized_dimensions_ids = {}


def load_line(first_line, line, year, sql_connection):
    mapped_line = get_mapped_line(line, dictionary_column_mapping[year], first_line)
    if mapped_line is None:
        return False
    participacao_values = {
        "fields": [],
        "values": []
    }
    for (table, value) in mapped_line.items():
        fields_string = '`,`'.join(value['fields'])
        values_insertions = ','.join(['?' for _ in value["values"]])
        string_values = '.'.join(value['values'])
        if f"{table}-{string_values}" not in memoized_dimensions_ids:
            query = f"insert into `{table}` (`{fields_string}`) values ({values_insertions})"
            sql_connection.execute(query, value["values"])
            memoized_dimensions_ids[f"{table}-{string_values}"] = sql_connection.lastrowid
        participacao_values["fields"].append(f"{table}_id")
        participacao_values["values"].append(memoized_dimensions_ids[f"{table}-{string_values}"])
    fields_string = '`,`'.join(participacao_values['fields'])
    values_insertions = ','.join(['?' for _ in participacao_values["values"]])
    query = f"insert into `participacao` (`{fields_string}`) values ({values_insertions})"
    sql_connection.execute(query, participacao_values["values"])
    return True


def load_data(year, filepath, sql_connection):
    data_table = open(filepath, 'r')
    first = True
    first_line = None
    count = 0
    for line in data_table:
        splitted_line = line.split(';')
        if first:
            first_line = splitted_line
            first = False
        elif load_line(first_line, splitted_line, year, sql_connection):
            count += 1
            b = f"Loading line {count}"
            print("\r", b, end="")
    print('\n')
    print('Total lines: ', count)


def connect_and_load(connection):
    print('Starting loading data')
    for year in dictionary_extracted_data:
        print(f"Loading {year} data")
        load_data(year, dictionary_extracted_data[year], connection.cursor())
        connection.commit()
    print('Database data loaded')


if __name__ == '__main__':
    print('Starting connection')
    connection = sqlite3.connect(database_root_path)
    connect_and_load(connection)
    print('Closing connection')
    connection.close()
