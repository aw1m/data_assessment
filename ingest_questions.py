import json
from datetime import datetime as dt
from ingestion_tools import clean_element
#
# "uuid": "8176b7e9-9a1d-4814-b04f-4195c48b7791",
# "type": "single-answer",
# "body": "meh",
# "has-correctness": true,
# "choice_uuid": "78b11006-c81c-46ad-9684-c36dcdbeb40e",
# "is-correct": true,
# "created-at": "2019-07-17T16:23:02.190Z",
# "deleted-at": null

def ingest_questions(cursor, sqliteConnection):
    with open("questions.json") as questions_file:
        questions_json = json.loads(questions_file.read())
        print(questions_json)
    for question in questions_json:
        question=  clean_element(question)
        # uuid,type,has_correctness,choice_uuid,is_correct,created_at,deleted_at = question.values()
#        if given_name is None or family_name is None or profession is None:
#             print("Record is incomplete: {}".format(str(question)))
#             pass
#
#         else:
#             cursor.execute("""
#             SELECT *
#             FROM users
#             WHERE username = ? """, [username])
#             if cursor.fetchall() == []:
#                 cursor.execute("""
#                 insert into users
#                 values ( ?,?,?,?,?);""", [username, given_name, family_name, profession, dt.now()])
#                 sqliteConnection.commit()
#
#             else:
#                 print("User already exist username:{} ".format(username))
#
#
#
#
#
# records = cursor.execute("SELECT * FROM users").fetchall()
# for record in records:
#     print(record)
