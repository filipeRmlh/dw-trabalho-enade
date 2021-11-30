import sqlite3

import pandas as pd
from dictionaries.paths_dict import database_root_path
from sklearn import metrics
from sklearn.model_selection import train_test_split as tsp
from sklearn.tree import DecisionTreeClassifier, export_text


def print_tree_text(tree):
    text_representation = export_text(tree)
    print("\n=========TREE GRAPH===========\n")
    print(text_representation)
    print("==============================\n")


def load_data_from_db(connection_cursor):
    result = connection_cursor.execute(
        "SELECT l.regiao, r.nivel, ng.nota FROM participacao "
        "join renda r on r.id = participacao.renda_id "
        "join localidade l on l.id = participacao.localidade_id "
        "join curso on curso.id = participacao.curso_id "
        "join idade i on i.id = participacao.idade_id "
        "join nota_geral ng on ng.id = participacao.nota_geral_id "
    ).fetchall()
    colnames = [description[0] for description in connection_cursor.description]
    return result, colnames


def load_data_into_pandas(data, col_names):
    sql_data = pd.DataFrame(data)
    sql_data.columns = col_names
    return sql_data


def split_x_y(pd_data, col_names):
    feature_cols = col_names[:-1]
    result_col = col_names[-1:]
    x = pd_data[feature_cols]
    y = pd_data[result_col]
    return x, y


def binarize_data(data):
    return pd.get_dummies(data)


def split_data_train(binarized_data, y):
    return tsp(binarized_data, y, train_size=0.80, test_size=0.20, random_state=0)


def get_trained_tree(x_train, y_train):
    print("Fitting training data")
    clf = DecisionTreeClassifier(criterion="gini")
    clf.fit(x_train, y_train)
    return clf


def test(trained_tree, x_test, y_test):
    y_pred = trained_tree.predict(x_test)
    print("Accuracy test:", metrics.accuracy_score(y_test, y_pred))
    print("Precision test:", metrics.precision_score(y_test, y_pred, average='micro'))


def treat_nota(value):
    if 0 <= value < 20:
        return "muito ruim"
    if 20 <= value < 50:
        return "ruim"
    if 50 <= value < 70:
        return "medio"
    if 70 <= value < 90:
        return "bom"
    if 90 <= value <= 100:
        return "muito bom"


def run_learning(sql_connection):
    print("Starting learning: Decision tree")
    db_data, db_head = load_data_from_db(sql_connection.cursor())
    pd_data = load_data_into_pandas(db_data, db_head)
    x, y = split_x_y(pd_data, db_head)
    ny = y.applymap(lambda x: treat_nota(x))
    binarized_data = binarize_data(x)
    x_train, x_test, y_train, y_test = split_data_train(binarized_data, ny)
    tree = get_trained_tree(x_train, y_train)
    test(tree, x_train, y_train)
    print_tree_text(tree)
    print("Learning finished")


if __name__ == '__main__':
    print('Starting connection')
    connection = sqlite3.connect(database_root_path)
    run_learning(connection)
    print('Closing connection')
    connection.close()
