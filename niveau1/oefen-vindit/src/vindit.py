'''Applicatie voor het beheren van verkopen bij Vind it!'''
import sqlite3

'''Verbind met lokale SQLite-database'''
verbinding = sqlite3.connect("db/vindit.db")
verbinding.row_factory = sqlite3.Row # om kolomnamen te kunnen gebruiken bij het tonen van data
verbinding.autocommit = True
cursor = verbinding.cursor()

