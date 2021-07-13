import json
from ingestion_tools import clean_element

def ingest_questionnaire_attempt(cursor, sqliteConnection):
    with open("questionnaire_attempt.json") as questionnaire_attempt_file:
        questionnaire_attempt_json = json.loads(questionnaire_attempt_file.read())
        # print(questionnaire_attempt_json)

    for questionnaire_attempt in questionnaire_attempt_json:
        clean_element(questionnaire_attempt)

        for key,value in questionnaire_attempt.items():
            print(key,":",value)
        break
        # uuid,type,body,has_correctness,choice_uuid,is_correct,created_at,deleted_at = question.values()
        # cursor.execute("""
        #      SELECT *
        #      FROM questionnaire_attempt q
        #      WHERE q.uuid = ?
        #  and q.choice_uuid = ?
        #  and q.deleted_at is null
        #  """, [uuid, choice_uuid])
        # records = cursor.fetchall()
        #
        # if records == []:
        #     cursor.execute("""
        #              insert into questionnaire_attempt
        #              values ( ?,?,?,?,?,?,?,?);""", [uuid,type,body,has_correctness,choice_uuid,is_correct,created_at,deleted_at])
        #     sqliteConnection.commit()
        # # else:
        # #     print("duplicate found: \ndb:{}\njson:{}\n\n".format(str(records), str(question)))
