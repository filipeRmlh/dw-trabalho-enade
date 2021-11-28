renda_mapping = {
    "A": "Menor que 1.5",
    "B": "De 1.5 a 3",
    "C": "De 3 a 4.5",
    "D": "De 4.5 a 6",
    "E": "De 6 a 10",
    "F": "De 10 a 30",
    "G": "Maior que 30",
}

dificuldade_mapping = {
    "A": "Muito fácil",
    "B": "Fácil",
    "C": "Médio",
    "D": "Difícil",
    "E": "Muito difícil",
    "*": "Resposta anulada",
    ".": "Não Respondido"
}

dificuldade_tipo_mapping = {
    "A": "Desconhecimento do conteúdo.",
    "B": "Forma diferente de abordagem do conteúdo.",
    "C": "Espaço insuficiente para responder às questões.",
    "D": "Falta de motivação para fazer a prova.",
    "E": "Não tive qualquer tipo de dificuldade para responder à prova.",
    "*": "Resposta anulada"
}

cota_tipo_mapping = {
    "A": "Não",
    "B": "Étnico-racial",
    "C": "Renda",
    "D": "Escola pública ou particular com bolsa",
    "E": "Dois ou mais critérios",
    "F": "Sistema diferente"
}

sexo_mapping = {
    "M": "Masculino",
    "F": "Feminino"
}

tempo_prova_mapping = {
    "A": "Muito longa",
    "B": "Longa",
    "C": "Adequada",
    "D": "Curta",
    "E": "Muito curta",
    "*": "Resposta anulada",
    ".": "Não Respondido"
}

em_tipo_mapping = {
    "A": "Publica",
    "B": "Privada",
    "C": "Exterior",
    "D": "Maior parte publica",
    "E": "Maior parte privada",
    "F": "Parte brasil e parte exterior"
}

uf_region_mapping = {
    "1": "Norte",
    "2": "Nordeste",
    "3": "Sudeste",
    "4": "Sul",
    "5": "Centro-Oeste"
}

uf_mapping = {
    "11": "RO",
    "12": "AC",
    "13": "AM",
    "14": "RR",
    "15": "PA",
    "16": "AP",
    "17": "TO",
    "21": "MA",
    "22": "PI",
    "23": "CE",
    "24": "RN",
    "25": "PB",
    "26": "PE",
    "27": "AL",
    "28": "SE",
    "29": "BA",
    "31": "MG",
    "32": "ES",
    "33": "RJ",
    "35": "SP",
    "41": "PR",
    "42": "SC",
    "43": "RS",
    "50": "MS",
    "51": "MT",
    "52": "GO",
    "53": "DF"
}

curso_nome_mapping = {
    "21": "ARQUITETURA E URBANISMO",
    "72": "TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS",
    "76": "TECNOLOGIA EM GESTÃO DA PRODUÇÃO INDUSTRIAL",
    "79": "TECNOLOGIA EM REDES DE COMPUTADORES",
    "701": "MATEMÁTICA (BACHARELADO)",
    "702": "MATEMÁTICA (LICENCIATURA)",
    "903": "LETRAS-PORTUGUÊS (BACHARELADO)",
    "904": "LETRAS-PORTUGUÊS (LICENCIATURA)",
    "905": "LETRAS-PORTUGUÊS E INGLÊS (LICENCIATURA)",
    "906": "LETRAS-PORTUGUÊS E ESPANHOL (LICENCIATURA)",
    "1401": "FÍSICA (BACHARELADO)",
    "1402": "FÍSICA (LICENCIATURA)",
    "1501": "QUÍMICA (BACHARELADO)",
    "1502": "QUÍMICA (LICENCIATURA)",
    "1601": "CIÊNCIAS BIOLÓGICAS (BACHARELADO)",
    "1602": "CIÊNCIAS BIOLÓGICAS (LICENCIATURA)",
    "2001": "PEDAGOGIA (LICENCIATURA)",
    "2401": "HISTÓRIA (BACHARELADO)",
    "2402": "HISTÓRIA (LICENCIATURA)",
    "2501": "ARTES VISUAIS (LICENCIATURA)",
    "3001": "GEOGRAFIA (BACHARELADO)",
    "3002": "GEOGRAFIA (LICENCIATURA)",
    "3201": "FILOSOFIA (BACHARELADO)",
    "3202": "FILOSOFIA (LICENCIATURA)",
    "3502": "EDUCAÇÃO FÍSICA (LICENCIATURA)",
    "4003": "ENGENHARIA DA COMPUTAÇÃO",
    "4004": "CIÊNCIA DA COMPUTAÇÃO (BACHARELADO)",
    "4005": "CIÊNCIA DA COMPUTAÇÃO (LICENCIATURA)",
    "4006": "SISTEMAS DE INFORMAÇÃO",
    "4301": "MÚSICA (LICENCIATURA)",
    "5401": "CIÊNCIAS SOCIAIS (BACHARELADO)",
    "5402": "CIÊNCIAS SOCIAIS (LICENCIATURA)",
    "5710": "ENGENHARIA CIVIL",
    "5806": "ENGENHARIA ELÉTRICA",
    "5814": "ENGENHARIA DE CONTROLE E AUTOMAÇÃO",
    "5902": "ENGENHARIA MECÂNICA",
    "6002": "ENGENHARIA DE ALIMENTOS",
    "6008": "ENGENHARIA QUÍMICA",
    "6208": "ENGENHARIA DE PRODUÇÃO",
    "6306": "ENGENHARIA",
    "6307": "ENGENHARIA AMBIENTAL",
    "6405": "ENGENHARIA FLORESTAL",
    "6407": "LETRAS - INGLÊS",
    "6409": "TECNOLOGIA EM GESTÃO DA TECNOLOGIA DA INFORMAÇÃO",
    "1": "ADMINISTRAÇÃO",
    "2": "DIREITO",
    "13": "CIÊNCIAS ECONÔMICAS",
    "18": "PSICOLOGIA",
    "22": "CIÊNCIAS CONTÁBEIS",
    "26": "DESIGN",
    "29": "TURISMO",
    "38": "SERVIÇO SOCIAL",
    "67": "SECRETARIADO EXECUTIVO",
    "81": "RELAÇÕES INTERNACIONAIS",
    "83": "TECNOLOGIA EM DESIGN DE MODA",
    "84": "TECNOLOGIA EM MARKETING",
    "85": "TECNOLOGIA EM PROCESSOS GERENCIAIS",
    "86": "TECNOLOGIA EM GESTÃO DE RECURSOS HUMANOS",
    "87": "TECNOLOGIA EM GESTÃO FINANCEIRA",
    "88": "TECNOLOGIA EM GASTRONOMIA",
    "93": "TECNOLOGIA EM GESTÃO COMERCIAL",
    "94": "TECNOLOGIA EM LOGÍSTICA",
    "100": "ADMINISTRAÇÃO PÚBLICA",
    "101": "TEOLOGIA",
    "102": "TECNOLOGIA EM COMÉRCIO EXTERIOR",
    "103": "TECNOLOGIA EM DESIGN DE INTERIORES",
    "104": "TECNOLOGIA EM DESIGN GRÁFICO",
    "105": "TECNOLOGIA EM GESTÃO DA QUALIDADE",
    "106": "TECNOLOGIA EM GESTÃO PÚBLICA",
    "803": "COMUNICAÇÃO SOCIAL - JORNALISMO",
    "804": "COMUNICAÇÃO SOCIAL - PUBLICIDADE E PROPAGANDA",
    "5": "MEDICINA VETERINÁRIA",
    "6": "ODONTOLOGIA",
    "12": "MEDICINA",
    "17": "AGRONOMIA",
    "19": "FARMÁCIA",
    "23": "ENFERMAGEM",
    "27": "FONOAUDIOLOGIA",
    "28": "NUTRIÇÃO",
    "36": "FISIOTERAPIA",
    "51": "ZOOTECNIA",
    "55": "BIOMEDICINA",
    "69": "TECNOLOGIA EM RADIOLOGIA",
    "90": "TECNOLOGIA EM AGRONEGÓCIOS",
    "91": "TECNOLOGIA EM GESTÃO HOSPITALAR",
    "92": "TECNOLOGIA EM GESTÃO AMBIENTAL",
    "95": "TECNOLOGIA EM ESTÉTICA E COSMÉTICA",
    "3501": "EDUCAÇÃO FÍSICA (BACHARELADO)",
    "6410": "TECNOLOGIA EM SEGURANÇA NO TRABALHO"
}
