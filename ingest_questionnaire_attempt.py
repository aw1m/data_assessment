import json
from ingestion_tools import clean_element

def ingest_questionnaire_attempt(cursor, sqliteConnection):
    with open("questionnaire_attempt.json") as questionnaire_attempt_file:
        questionnaire_attempt_json = json.loads(questionnaire_attempt_file.read())
        # print(questionnaire_attempt_json)

    for questionnaire_attempt in questionnaire_attempt_json:
        clean_element(questionnaire_attempt)
        # print(questionnaire_attempt)
        # l = list(questionnaire_attempt.keys())
        # new_l=[]
        # for e in l:
        #     e = str(e).replace("-","_")
        #     new_l.append("and q.{}=?".format(e))
        # [print(x) for x in new_l]
        # break

        user_uuid, activity_uuid, questionnaire_uuid, attempt_number,\
        submitted_at, created_at, updated_at, deleted_at, context_uuid, \
        question_uuid, confidence, type, single_answer_choice_uuid = questionnaire_attempt.values()
        cursor.execute("""
             SELECT *
             FROM questionnaire_attempt q
             WHERE  q.user_uuid=?
        and q.activity_uuid=?
        and q.questionnaire_uuid=?
        and q.attempt_number=?
        -- and q.submitted_at=?
        and q.created_at =?
        -- and ( q.updated_at <= ?
        -- or q.deleted_at<= ?)
        and q.context_uuid=?
        and q.question_uuid=?
        -- and q.confidence=?
        -- and q.type=?
        and q.single_answer_choice_uuid=?

         """, [user_uuid, activity_uuid, questionnaire_uuid, attempt_number,
        # submitted_at,
               created_at,
               # updated_at, deleted_at,
        context_uuid,question_uuid,
               # confidence, type,
               single_answer_choice_uuid])
        records = cursor.fetchall()

        if records == []:
            try:
                cursor.execute("""
                     insert into questionnaire_attempt
                     values ( ?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                           [user_uuid, activity_uuid, questionnaire_uuid, attempt_number, submitted_at, created_at,
                            updated_at, deleted_at, context_uuid,question_uuid, confidence, type,
                            single_answer_choice_uuid])
                sqliteConnection.commit()
            except Exception as e:
                print(e)
        else:
            db_updated_at = records[0][6]
            if db_updated_at is None and updated_at is not None:
                try:
                    cursor.execute("""
                                            delete 
                                            FROM questionnaire_attempt 
                                            WHERE  user_uuid=?
                                            and activity_uuid=?
                                            and questionnaire_uuid=?
                                            and attempt_number=?
                                            and created_at =?
                                            and updated_at is Null
                                            and context_uuid=?
                                            and question_uuid=?
                                            and single_answer_choice_uuid=?;
                                             """,
                                   [user_uuid, activity_uuid, questionnaire_uuid, attempt_number,created_at,
                                    context_uuid, question_uuid,single_answer_choice_uuid])
                    sqliteConnection.commit()
                    cursor.execute("""
                         insert into questionnaire_attempt
                         values ( ?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                   [user_uuid, activity_uuid, questionnaire_uuid, attempt_number, submitted_at,
                                    created_at,
                                    updated_at, deleted_at, context_uuid, question_uuid, confidence, type,
                                    single_answer_choice_uuid])
                    sqliteConnection.commit()
                except Exception as e:
                    print(e)
            elif  db_updated_at is not None and db_updated_at < updated_at:
                try:
                    cursor.execute("""
                                        delete 
                                        FROM questionnaire_attempt 
                                        WHERE  user_uuid=?
                                        and activity_uuid=?
                                        and questionnaire_uuid=?
                                        and attempt_number=?
                                        and created_at =?
                                        and updated_at <?
                                        and context_uuid=?
                                        and question_uuid=?
                                        and single_answer_choice_uuid=?;
                                         """,
                                   [user_uuid, activity_uuid, questionnaire_uuid, attempt_number, created_at,updated_at,
                                    context_uuid, question_uuid, single_answer_choice_uuid])
                    sqliteConnection.commit()
                    cursor.execute("""
                     insert into questionnaire_attempt
                     values ( ?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                   [user_uuid, activity_uuid, questionnaire_uuid, attempt_number, submitted_at,
                                    created_at,
                                    updated_at, deleted_at, context_uuid, question_uuid, confidence, type,
                                    single_answer_choice_uuid])
                    sqliteConnection.commit()
                except Exception as e:
                    print(e)
            # else:
            #     print("duplicate found : \ndb:{}\njs:{}\n\n".format(str(records), str([user_uuid, activity_uuid, questionnaire_uuid, attempt_number, submitted_at, created_at,
            #                 updated_at, deleted_at, context_uuid,question_uuid, confidence, type,
            #                 single_answer_choice_uuid])))

