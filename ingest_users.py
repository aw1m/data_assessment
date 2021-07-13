import json
from datetime import datetime as dt
from ingestion_tools import clean_element

def ingest_users(cursor, sqliteConnection):
    with open("users.json") as users_file:
        user_json = json.loads(users_file.read())
        # print(user_json)
    for user in user_json:
        user = clean_element(user)
        username, given_name, family_name, profession = user.values()
        if given_name is None or family_name is None or profession is None:
            print("Record is incomplete: {}".format(str(user)))
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
                print("User already exist username:{} ".format(username))