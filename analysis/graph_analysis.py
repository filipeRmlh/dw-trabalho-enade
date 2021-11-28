import sqlite3
import matplotlib.pyplot as plt
from dictionaries.paths_dict import database_root_path


def plot_barh(title, marks, names, fig_size=(9, 5)):
    plt.rcParams["figure.figsize"] = fig_size
    plt.barh(names["values"], marks["values"])
    plt.ylabel(names["label"])
    plt.xlabel(marks["label"])
    plt.title(title)
    plt.show()


def plot_bar(title, marks, names, fig_size=(5, 9)):
    plt.rcParams["figure.figsize"] = fig_size
    plt.bar(names["values"], marks["values"])
    plt.xlabel(names["label"])
    plt.ylabel(marks["label"])
    plt.title(title)
    plt.show()


# Qual a nota, em geral dos participantes do enade por sexo
def notas_homens_vs_mulheres(connection_cursor):
    query = "SELECT sexo, avg(nota) as avgnota FROM sexo, nota_geral, participacao as p where " \
            "p.nota_geral_id = nota_geral.id and p.sexo_id = sexo.id  group  by sexo.id order by nota"
    result = connection_cursor.execute(query).fetchall()
    avgNota = []
    sexo = []
    for i in result:
        sexo.append(i[0])
        avgNota.append(i[1])
    plot_bar("Notas entre Homens e Mulheres", {"label": "media de nota", "values": avgNota},
             {"label": "sexo", "values": sexo})


# Qual a proporção de participação entre homens e mulheres
def participacao_homens_mulheres(connection_cursor):
    query = "SELECT sexo, count(p.sexo_id) as sexocount FROM sexo, participacao as p where " \
            "p.nota_geral_id = sexo.id  group  by sexo.id order by sexo"
    result = connection_cursor.execute(query).fetchall()
    participants = []
    sexo = []
    total = 0
    for i in result:
        total += int(i[1])
    for i in result:
        sexo.append(i[0])
        participants.append(float(i[1]) / total)
    plot_bar("Relação Sexo x Participantes", {"label": "numero de participantes", "values": participants},
             {"label": "sexo", "values": sexo})


# Qual o rankeamento de participação dos cursos
def participacao_curso(connection_cursor):
    query = "SELECT nome, count(p.curso_id) as cursocount FROM curso, participacao as p where " \
            "p.curso_id = curso.id  group  by curso.id order by cursocount"
    result = connection_cursor.execute(query).fetchall()
    participants = []
    degree = []
    for i in result:
        degree.append(i[0])
        participants.append(i[1])
    plot_barh("Participação geral dos cursos", {"label": "numero de participantes", "values": participants},
              {"label": "curso", "values": degree}, fig_size=(40, 20))


# Qual a média de notas por faixa de renda
def relacao_renda_nota_media(connection_cursor):
    query = "SELECT nivel, avg(nota) as avgnota FROM renda, nota_geral, participacao as p where " \
            "p.nota_geral_id = nota_geral.id and p.renda_id = renda.id  group by renda.id order by avgnota"
    result = connection_cursor.execute(query).fetchall()
    participants = []
    degree = []
    for i in result:
        degree.append(i[0])
        participants.append(i[1])
    plot_bar("Nota média por renda no enade", {"label": "nota média", "values": participants},
             {"label": "faixa de renda (sal. mínimo)", "values": degree}, fig_size=(12, 5))



def media_notas_nos_estados(connection_cursor):
    query = "SELECT uf, avg(nota) as avgnota FROM localidade, nota_geral, participacao as p where " \
            "p.nota_geral_id = nota_geral.id and p.localidade_id = localidade.id  group  by uf, regiao order by avgnota"
    result = connection_cursor.execute(query).fetchall()
    avgNota = []
    uf = []
    for i in result:
        uf.append(i[0])
        avgNota.append(i[1])
    plot_barh("Media de notas por estado", {"label": "media de nota", "values": avgNota},
             {"label": "UF", "values": uf})


def generate_plots(connection_cursor):
    notas_homens_vs_mulheres(connection_cursor)
    participacao_homens_mulheres(connection_cursor)
    participacao_curso(connection_cursor)
    relacao_renda_nota_media(connection_cursor)
    media_notas_nos_estados(connection_cursor)


if __name__ == '__main__':
    print('Starting connection')
    connection = sqlite3.connect(database_root_path)
    generate_plots(connection.cursor())
    print('Closing connection')
    connection.close()
