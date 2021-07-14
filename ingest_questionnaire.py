import json
from ingestion_tools import clean_element, write_not_proccessed
from datetime import datetime as dt


def ingest_questionnaire(cursor, sqliteConnection):
    with open("questionnaire.json") as questionnaire_file:
        questionnaire_json = json.loads(questionnaire_file.read())

    not_processed=[]
    for questionnaire in questionnaire_json:
        clean_element(questionnaire)
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
                     values ( ?,?,?,?,?,?);""", [ uuid,question_uuid,name,context,is_required,dt.now()])#
            sqliteConnection.commit()
        else:
            not_processed.append(questionnaire)
    write_not_proccessed('questionnaire_not_processed.json' ,not_processed)
    return not_processed
