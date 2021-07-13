import sqlite3
import ingest_users
from ingest_questions import ingest_questions
import json
from ingestion_tools import clean_element

sqliteConnection = sqlite3.connect('data_assessment.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")
with open("model.sql")  as query:
    cursor.executescript(query.read())
    sqliteConnection.commit()

# ingest_users(cursor, sqliteConnection)
# ingest_questions(cursor, sqliteConnection)
#

ingest_questions(cursor, sqliteConnection)
records = cursor.execute("SELECT * FROM questions").fetchall()
for record in records:
    print(record)