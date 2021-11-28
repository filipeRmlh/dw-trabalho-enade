-- noinspection SqlNoDataSourceInspectionForFile

CREATE TABLE IF NOT EXISTS `idade`(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    idade INTEGER UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `sexo` (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    sexo TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `localidade` (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    regiao TEXT NOT NULL,
    uf TEXT NOT NULL,
    CONSTRAINT regiao_uf_unique UNIQUE (regiao, uf)
);

CREATE TABLE IF NOT EXISTS `dificuldade_tipo` (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tipo TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `dificuldade_fg` (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nivel TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `dificuldade_ce` (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nivel TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `tempo_prova` (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tempo_faixa TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `nota_geral` (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nota REAL UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `cota` (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tipo TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `ensino_medio`(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tipo_escola TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `curso`(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS `enade`(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ano INTEGER UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `renda`(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nivel TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS `participacao`(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    idade_id INTEGER NOT NULL,
    sexo_id INTEGER NOT NULL,
    localidade_id INTEGER NOT NULL,
    dificuldade_fg_id INTEGER NOT NULL,
    dificuldade_ce_id INTEGER NOT NULL,
    dificuldade_tipo_id INTEGER NOT NULL,
    tempo_prova_id INTEGER NOT NULL,
    cota_id INTEGER NOT NULL,
    nota_geral_id INTEGER NOT NULL,
    ensino_medio_id INTEGER NOT NULL,
    curso_id INTEGER NOT NULL,
    enade_id INTEGER NOT NULL,
    renda_id INTEGER NOT NULL,
    FOREIGN KEY (idade_id) references idade(id) on delete cascade ,
    FOREIGN KEY (sexo_id) references sexo(id) on delete cascade,
    FOREIGN KEY (localidade_id) references localidade(id) on delete cascade,
    FOREIGN KEY (dificuldade_fg_id) references dificuldade_fg(id) on delete cascade,
    FOREIGN KEY (dificuldade_ce_id) references dificuldade_ce(id) on delete cascade,
    FOREIGN KEY (dificuldade_tipo_id) references dificuldade_tipo(id) on delete cascade,
    FOREIGN KEY (tempo_prova_id) references tempo_prova(id) on delete cascade,
    FOREIGN KEY (cota_id) references cota(id) on delete set null,
    FOREIGN KEY (nota_geral_id) references nota_geral(id) on delete cascade,
    FOREIGN KEY (ensino_medio_id) references ensino_medio(id) on delete cascade,
    FOREIGN KEY (curso_id) references curso(id) on delete cascade,
    FOREIGN KEY (enade_id) references enade(id) on delete cascade,
    FOREIGN KEY (renda_id) references renda(id) on delete cascade
);