import json
from ingestion_tools import clean_element,write_not_proccessed

def ingest_questions(cursor, sqliteConnection):
    with open("questions.json") as questions_file:
        questions_json = json.loads(questions_file.read())
        # print(questions_json)
    not_processed = []
    for question in questions_json:
        clean_element(question)

        # print(question)
        uuid,type,body,has_correctness,choice_uuid,is_correct,created_at,deleted_at = question.values()
        cursor.execute("""
             SELECT *
             FROM questions q
             WHERE q.uuid = ? 
         and q.choice_uuid = ?
         and q.deleted_at is null
         """, [uuid, choice_uuid])
        records = cursor.fetchall()

        if records == []:
            cursor.execute("""
                     insert into questions
                     values ( ?,?,?,?,?,?,?,?);""", [uuid,choice_uuid,type,body,has_correctness,is_correct,created_at,deleted_at])
            sqliteConnection.commit()
        else:
            not_processed.append(question)
    write_not_proccessed('questionnaire_not_processed.json', not_processed)
    return not_processed