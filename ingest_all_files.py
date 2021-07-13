import sqlite3
import ingest_users
from ingest_questions import ingest_questions
import json
from ingestion_tools import clean_element
from ingest_questionnaire import ingest_questionnaire

sqliteConnection = sqlite3.connect('data_assessment.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")
with open("model.sql")  as query:
    cursor.executescript(query.read())
    sqliteConnection.commit()

# ingest_users(cursor, sqliteConnection)
# ingest_questions(cursor, sqliteConnection)
#
#
ingest_questionnaire(cursor, sqliteConnection)
# records = cursor.execute("SELECT * FROM questionnaire").fetchall()
# for record in records:
#     print(record)