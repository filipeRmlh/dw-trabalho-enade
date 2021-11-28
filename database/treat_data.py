from dictionaries.data_values_dict import *


def treat_renda(renda):
    if renda in renda_mapping:
        return renda_mapping[renda]
    return "N/A"


def treat_dificuldade_nivel(dificuldade):
    if dificuldade in dificuldade_mapping:
        return dificuldade_mapping[dificuldade]
    return "N/A"


def treat_tempo_prova(tempo_prova):
    if tempo_prova in tempo_prova_mapping:
        return tempo_prova_mapping[tempo_prova]
    return "N/A"


def treat_em_tipo(em_tipo):
    if em_tipo in em_tipo_mapping:
        return em_tipo_mapping[em_tipo]
    return "N/A"


def treat_regiao(regiao):
    if regiao in uf_region_mapping:
        return uf_region_mapping[regiao]
    return "N/A"


def treat_uf(uf):
    if uf in uf_mapping:
        return uf_mapping[uf]
    return "N/A"


def treat_nota(nota):
    if nota.strip() in {None, '', ".", "*", "NA"}:
        return "N/A"
    nota_value = float(nota.replace(',', '.'))
    return str(nota_value)


def treat_cota_tipo(cota):
    if cota in cota_tipo_mapping:
        return cota_tipo_mapping[cota]
    return "N/A"


def treat_dificuldade_tipo(dificuldade_tipo):
    if dificuldade_tipo in dificuldade_tipo_mapping:
        return dificuldade_tipo_mapping[dificuldade_tipo]
    return "N/A"


def treat_sexo(sexo):
    if sexo in sexo_mapping:
        return sexo_mapping[sexo]
    return "N/A"


def treat_curso_nome(curso_id):
    if curso_id in curso_nome_mapping:
        return curso_nome_mapping[curso_id]
    return "N/A"


treat_func_dispatcher = {
    "renda": {
        "nivel": treat_renda
    },
    "ensino_medio": {
        "tipo_escola": treat_em_tipo,
        "uf": treat_uf
    },
    "localidade": {
        "uf": treat_uf,
        "regiao": treat_regiao
    },
    "nota_geral": {
        "nota": treat_nota,
    },
    "dificuldade_fg": {
        "nivel": treat_dificuldade_nivel
    },
    "dificuldade_ce": {
        "nivel": treat_dificuldade_nivel
    },
    "tempo_prova": {
        "tempo_faixa": treat_tempo_prova
    },
    "dificuldade_tipo": {
        "tipo": treat_dificuldade_tipo
    },
    "cota": {
        "tipo": treat_cota_tipo
    },
    "curso": {
        "nome": treat_curso_nome
    },
    "sexo": {
        "sexo": treat_sexo
    }
}


def treat_data(table, field, value):
    if table in treat_func_dispatcher:
        if field in treat_func_dispatcher[table]:
            return treat_func_dispatcher[table][field](value)
    return value
