PRAGMA foreign_keys = ON;

-- Verwijder tabellen in de juiste volgorde als ze al bestaan (ivm constraints)
DROP TABLE IF EXISTS onderhoudslog;
DROP TABLE IF EXISTS onderhoudstype;
DROP TABLE IF EXISTS attractie;

-- 1. Tabel voor de attracties
CREATE TABLE attractie (
    naam VARCHAR(100) NOT NULL PRIMARY KEY,
    bouwjaar INT NOT NULL,
    locatie VARCHAR(100) NOT NULL,
    omschrijving TEXT NULL
);

-- 2. Tabel voor de categorieën van onderhoud
CREATE TABLE onderhoudstype (
    naam VARCHAR(100) NOT NULL PRIMARY KEY,
    is_veiligheidskritisch TINYINT(1) NOT NULL,
    omschrijving TEXT NULL
);

-- 3. Tabel voor de onderhoudsbeurten (de log)
CREATE TABLE onderhoudslog (
    attractie VARCHAR(100) NOT NULL,
    onderhoudstype VARCHAR(100) NOT NULL,
    datum DATE NOT NULL,
    dagen_buiten_bedrijf INT NOT NULL,
    PRIMARY KEY (attractie, onderhoudstype, datum),
    CONSTRAINT fk_log_attractie FOREIGN KEY (attractie)
        REFERENCES attractie(naam),
    CONSTRAINT fk_log_type FOREIGN KEY (onderhoudstype)
        REFERENCES onderhoudstype(naam)
);