PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS lijst;
DROP TABLE IF EXISTS winkel;

CREATE TABLE IF NOT EXISTS "winkel" (
    "naam" VARCHAR NOT NULL,
    "verzendkosten" REAL,
    PRIMARY KEY("naam")
);

CREATE TABLE IF NOT EXISTS "lijst" (
    "naam" VARCHAR NOT NULL,
    "budget_limiet" REAL,
    PRIMARY KEY("naam")
);

CREATE TABLE IF NOT EXISTS "item" (
    "titel" VARCHAR NOT NULL,
    "prijs" REAL NOT NULL,
    "prioriteit" INTEGER,
    "lijst" VARCHAR NOT NULL,
    "winkel" VARCHAR,
    PRIMARY KEY("titel", "lijst"),
    FOREIGN KEY ("lijst") REFERENCES "lijst"("naam")
        ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY ("winkel") REFERENCES "winkel"("naam")
        ON UPDATE NO ACTION ON DELETE NO ACTION
);