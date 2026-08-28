PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Onderdeel;
DROP TABLE IF EXISTS Scenario;
DROP TABLE IF EXISTS Leverancier;

CREATE TABLE Leverancier (
    naam VARCHAR(100) NOT NULL PRIMARY KEY,
    transportkosten DECIMAL(6, 2) NOT NULL DEFAULT 0.00
);

CREATE TABLE Scenario (
    naam VARCHAR(50) NOT NULL PRIMARY KEY,
    budget_limiet DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Onderdeel (
    scenario VARCHAR(50) NOT NULL,
    titel VARCHAR(100) NOT NULL,
    prijs DECIMAL(10, 2) NOT NULL,
    leverancier VARCHAR(100),
    prioriteit INT NOT NULL,
    PRIMARY KEY (scenario, titel),
    FOREIGN KEY (leverancier) REFERENCES Leverancier(naam),
    FOREIGN KEY (scenario) REFERENCES Scenario(naam)
);
