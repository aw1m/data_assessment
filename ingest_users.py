import json
from datetime import datetime as dt
from ingestion_tools import clean_element,write_not_proccessed

def ingest_users(cursor, sqliteConnection):
    with open("users.json") as users_file:
        user_json = json.loads(users_file.read())

    not_processed = []
    for user in user_json:
        user = clean_element(user)
        username, given_name, family_name, profession = user.values()
        if given_name is None or family_name is None or profession is None:
            not_processed.append(user)
            pass

        else:
            cursor.execute("""
            SELECT * 
            FROM users 
            WHERE username = ? """, [username])
            if cursor.fetchall() == []:
                cursor.execute("""
                insert into users
                values ( ?,?,?,?,?);""", [username, given_name, family_name, profession, dt.now()])
                sqliteConnection.commit()

            else:
                not_processed.append(user)
    write_not_proccessed('user_not_processed.json', not_processed)
    return not_processed
