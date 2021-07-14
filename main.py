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


#check users
cursor.execute("""
 SELECT count(*)
 FROM questionnaire_attempt qt
    left join users u
    on qt.user_uuid= u.username
    where u.username is null;
""")
records = cursor.fetchall()
for record in records:
    print(record)


#check questions
cursor.execute("""
 SELECT count(*)
 FROM questionnaire_attempt qt
    left join questions q
    on q.uuid= qt.question_uuid
       and q.choice_uuid =qt.single_answer_choice_uuid
    where q.uuid is null;
""")
records = cursor.fetchall()
for record in records:
    print(record)

cursor.execute("""
 SELECT *
 FROM  questions q
where q.uuid= 'add7e26f-9b14-4d40-aa35-45a852ca94af';
""")
records = cursor.fetchall()
for record in records:
    print(record)



#check questionnaire
cursor.execute("""
 SELECT *
 FROM questionnaire_attempt qt
    left join questionnaire q
    on q.uuid= qt.questionnaire_uuid
    where q.uuid is null;
""")
records = cursor.fetchall()
for record in records:
    print(record)


cursor.close()
sqliteConnection.close()
