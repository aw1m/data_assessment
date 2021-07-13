import json
from ingestion_tools import clean_element

def ingest_questionnaire(cursor, sqliteConnection):
    with open("questionnaire.json") as questionnaire_file:
        questionnaire_json = json.loads(questionnaire_file.read())
        # print(questions_json)

    for questionnaire in questionnaire_json:
        clean_element(questionnaire)

        # print(question)
        # uuid,type,body,has_correctness,choice_uuid,is_correct,created_at,deleted_at = question.values()
        # cursor.execute("""
        #      SELECT *
        #      FROM questions q
        #      WHERE q.uuid = ?
        #  and q.choice_uuid = ?
        #  and q.deleted_at is null
        #  """, [uuid, choice_uuid])
        # records = cursor.fetchall()
        #
        # if records == []:
        #     cursor.execute("""
        #              insert into questions
        #              values ( ?,?,?,?,?,?,?,?);""", [uuid,type,body,has_correctness,choice_uuid,is_correct,created_at,deleted_at])#dt.now()
        #     sqliteConnection.commit()
        # # else:
        # #     print("duplicate found: \ndb:{} \n json:{}\n\n".format(str(records), str(question)))
