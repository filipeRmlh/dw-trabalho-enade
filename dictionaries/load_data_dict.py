# dictionary_mapping format:
# {
#     <CsvYear> : {
#         <CsvColumnName>: (<SqlTableName>, <SqlTableField>),
#         ...
#     }
#     ...
# }
dictionary_column_mapping = {
    '2017': {
        'NU_IDADE': ('idade', 'idade'),
        'TP_SEXO': ('sexo', 'sexo'),
        'CO_REGIAO_CURSO': ('localidade', 'regiao'),
        'CO_UF_CURSO': ('localidade', 'uf'),
        'CO_RS_I1': ('dificuldade_fg', 'nivel'),
        'CO_RS_I2': ('dificuldade_ce', 'nivel'),
        'CO_RS_I7': ('dificuldade_tipo', 'tipo'),
        'CO_RS_I3': ('tempo_prova', 'tempo_faixa'),
        'NT_GER': ('nota_geral', 'nota'),
        'QE_I15': ('cota', 'tipo'),
        'QE_I17': ('ensino_medio', 'tipo_escola'),
        'CO_GRUPO': ('curso', 'nome'),
        'NU_ANO': ('enade', 'ano'),
        'QE_I08': ('renda', 'nivel')
    },
    '2018': {
        'NU_IDADE': ('idade', 'idade'),
        'TP_SEXO': ('sexo', 'sexo'),
        'CO_REGIAO_CURSO': ('localidade', 'regiao'),
        'CO_UF_CURSO': ('localidade', 'uf'),
        'CO_RS_I1': ('dificuldade_fg', 'nivel'),
        'CO_RS_I2': ('dificuldade_ce', 'nivel'),
        'CO_RS_I7': ('dificuldade_tipo', 'tipo'),
        'CO_RS_I3': ('tempo_prova', 'tempo_faixa'),
        'NT_GER': ('nota_geral', 'nota'),
        'QE_I15': ('cota', 'tipo'),
        'QE_I17': ('ensino_medio', 'tipo_escola'),
        'CO_GRUPO': ('curso', 'nome'),
        'NU_ANO': ('enade', 'ano'),
        'QE_I08': ('renda', 'nivel')
    },
    '2019': {
        'NU_IDADE': ('idade', 'idade'),
        'TP_SEXO': ('sexo', 'sexo'),
        'CO_REGIAO_CURSO': ('localidade', 'regiao'),
        'CO_UF_CURSO': ('localidade', 'uf'),
        'CO_RS_I1': ('dificuldade_fg', 'nivel'),
        'CO_RS_I2': ('dificuldade_ce', 'nivel'),
        'CO_RS_I7': ('dificuldade_tipo', 'tipo'),
        'CO_RS_I3': ('tempo_prova', 'tempo_faixa'),
        'NT_GER': ('nota_geral', 'nota'),
        'QE_I15': ('cota', 'tipo'),
        'QE_I17': ('ensino_medio', 'tipo_escola'),
        'CO_GRUPO': ('curso', 'nome'),
        'NU_ANO': ('enade', 'ano'),
        'QE_I08': ('renda', 'nivel')
    },
}