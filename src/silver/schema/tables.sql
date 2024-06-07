-- Criação da tabela de municípios
CREATE TABLE municipios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

-- Criação da tabela de postos
CREATE TABLE postos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    municipio_id INT REFERENCES municipios(id)
);

-- Criação da tabela de registros
CREATE TABLE registros (
    id SERIAL PRIMARY KEY,
    posto_id INT REFERENCES postos(id),
    data DATE NOT NULL,
	registro float NOT NULL
);
