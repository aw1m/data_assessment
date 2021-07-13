import sqlite3
import ingest_users
from ingest_questions import ingest_questions

sqliteConnection = sqlite3.connect('data_assessment.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")
with open("model.sql")  as query:
    cursor.executescript(query.read())
    sqliteConnection.commit()

# ingest_users(cursor, sqliteConnection)
ingest_questions(cursor, sqliteConnection)

