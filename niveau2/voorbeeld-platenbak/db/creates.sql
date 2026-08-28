PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS track;
DROP TABLE IF EXISTS artiest;
DROP TABLE IF EXISTS genre;


CREATE TABLE genre (
    naam CHAR(15) NOT NULL PRIMARY KEY,
    omschrijving VARCHAR(255)
);

CREATE TABLE artiest (
    naam VARCHAR(255) NOT NULL PRIMARY KEY,
    land VARCHAR(255) NOT NULL
);

CREATE TABLE track (
    artiest VARCHAR(255) NOT NULL,
    titel VARCHAR(255) NOT NULL,
    genre CHAR(15) NOT NULL,
    duur INT NOT NULL,
    jaar INT NOT NULL,
    PRIMARY KEY (artiest, titel),
    FOREIGN KEY (artiest) REFERENCES artiest(naam),
    FOREIGN KEY (genre) REFERENCES genre(naam)
);