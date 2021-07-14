import sqlite3

from ingest_users import ingest_users
from ingest_questions import ingest_questions
from ingest_questionnaire import ingest_questionnaire
from ingest_questionnaire_attempt import ingest_questionnaire_attempt

sqliteConnection = sqlite3.connect('data_assessment.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")
with open("model.sql")  as query:
    cursor.executescript(query.read())
    sqliteConnection.commit()

ingest_users(cursor, sqliteConnection)
print("Proccessed Users")
ingest_questions(cursor, sqliteConnection)
print("Proccessed Questions")
ingest_questionnaire(cursor, sqliteConnection)
print("Proccessed Questionnaire")
ingest_questionnaire_attempt(cursor, sqliteConnection)
print("Proccessed Questionnaire Attempts")



cursor.execute("""
 SELECT * 
 FROM questionnaire_attempt qt
    left join users u
    on qt.user_uuid= u.username
    where u.username is null;
""")
records = cursor.fetchall()
for record in records:
    print(record)

cursor.close()
sqliteConnection.close()
