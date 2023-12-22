DROP TABLE IF EXISTS Animais;
DROP TABLE IF EXISTS Especies;

CREATE TABLE Especies (
    ID_Especie INTEGER PRIMARY KEY,
    Especie TEXT NOT NULL UNIQUE,
    Descricao TEXT
);

CREATE TABLE Animais (
    ID_Animal INTEGER PRIMARY KEY,
    Animal TEXT NOT NULL,
    Nome TEXT NOT NULL,
    Idade INTEGER NOT NULL,
    Data_Entrada DATE NOT NULL,
    Especie INTEGER,
    FOREIGN KEY(Especie) REFERENCES Especies(Especie)
);
