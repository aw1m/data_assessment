import json
from ingestion_tools import clean_element
from datetime import datetime as dt

# {
#     "uuid": "c5e631c1-421d-48f4-b696-75fb18ca7084",
#     "name": null,
#     "context": "post-test",
#     "question-uuid": "7caecaa5-110f-4785-8bdb-5837ce584766",
#     "is-required": true
# },
def ingest_questionnaire(cursor, sqliteConnection):
    with open("questionnaire.json") as questionnaire_file:
        questionnaire_json = json.loads(questionnaire_file.read())
        # print(questionnaire_json)

    for questionnaire in questionnaire_json:
        clean_element(questionnaire)

        # print(questionnaire)

        uuid,name,context,question_uuid,is_required = questionnaire.values()
        cursor.execute("""
             SELECT *
             FROM questionnaire q
             WHERE q.uuid = ?
         and q.question_uuid = ?
         """, [uuid, question_uuid])
        records = cursor.fetchall()

        if records == []:
            cursor.execute("""
                     insert into questionnaire
                     values ( ?,?,?,?,?,?);""", [ uuid,name,context,question_uuid,is_required,dt.now()])#
            sqliteConnection.commit()
        else:
            print("duplicate found: \ndb:{}\njson:{}\n\n".format(str(records), str(questionnaire)))
