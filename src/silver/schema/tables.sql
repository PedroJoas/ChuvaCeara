-- Criação da tabela de municípios
CREATE TABLE municipios (
    id_municipio SERIAL PRIMARY KEY,
    Municipios VARCHAR(255) NOT NULL
);

-- Criação da tabela de postos
CREATE TABLE postos (
    id_posto SERIAL PRIMARY KEY,
    Postos VARCHAR(255) NOT NULL,
    id_municipio INT REFERENCES municipios(id_municipio),
	Latitude DECIMAL(9,6),
    Longitude DECIMAL(9,6)
);

-- Criação da tabela de registros
CREATE TABLE registros (
    id_registro SERIAL PRIMARY KEY,
    id_posto INT REFERENCES postos(id_posto),
    data DATE NOT NULL,
	registros float NOT NULL
);




