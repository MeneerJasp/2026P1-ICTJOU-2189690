PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS persoon_hobby;
DROP TABLE IF EXISTS persoon;
DROP TABLE IF EXISTS hobby;

CREATE TABLE persoon (
    naam VARCHAR(50) NOT NULL PRIMARY KEY,
    afstand DECIMAL(3,1) NOT NULL
);

CREATE TABLE hobby (
    naam VARCHAR(50) NOT NULL PRIMARY KEY,
    individuele_hobby TINYINT(1) NOT NULL,
    omschrijving TEXT NOT NULL
);

CREATE TABLE persoon_hobby (
    persoon_naam VARCHAR(50) NOT NULL,
    hobby_naam VARCHAR(50) NOT NULL,
    volgorde INT NOT NULL,
    PRIMARY KEY(persoon_naam, volgorde),
    FOREIGN KEY (persoon_naam) REFERENCES persoon(naam),
    FOREIGN KEY (hobby_naam) REFERENCES hobby(naam)
);