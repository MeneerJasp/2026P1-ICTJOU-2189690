CREATE TABLE IF NOT EXISTS "elftal" (
	"elftalcode" VARCHAR NOT NULL,
	"omschrijving" VARCHAR NOT NULL,
	"coach" VARCHAR NOT NULL,
	"maximumleeftijd" INTEGER NOT NULL,
	PRIMARY KEY("elftalcode")
);

CREATE TABLE IF NOT EXISTS "speler" (
	"speler_id" INTEGER NOT NULL,
	"naam" VARCHAR NOT NULL,
	"elftal" VARCHAR NOT NULL,
	"positie" VARCHAR NOT NULL,
	"leeftijd" INTEGER NOT NULL,
	PRIMARY KEY("speler_id"),
	FOREIGN KEY ("elftal") REFERENCES "elftal"("elftalcode")
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY ("positie") REFERENCES "positie"("naam")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "positie" (
	"naam" VARCHAR NOT NULL,
	PRIMARY KEY("naam")
);