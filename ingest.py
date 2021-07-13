import json
import sqlite3
from datetime import datetime as dt

def remove_missing_strings(string:str):
    if string is None:
        return string
    string = string.strip()
    if string =="" or string=="none":
        string =None
    return string

def clean_element(element:dict):
    for key, value in element.items():
        element[key] = remove_missing_strings(value)
    return element


sqliteConnection = sqlite3.connect('data_assessment.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")
with open("model.sql")  as query:
    cursor.executescript(query.read())
    sqliteConnection.commit()

with open("users.json") as users_file:
    user_json = json.loads(users_file.read())
    # print(user_json)
for user in user_json:
    clean_element(user)
    username,given_name,family_name, profession =user.values()
    if given_name is None or family_name is None or profession is None:
        print("Record is incomplete: {}".format(str(user)))
        pass

    else:
        cursor.execute("""
        SELECT * 
        FROM users 
        WHERE username = ? """, [username])
        if cursor.fetchall()==[] :
            cursor.execute("""
            insert into users
            values ( ?,?,?,?,?);""",[username,given_name,family_name,profession, dt.now()])
            sqliteConnection.commit()
        else:
            print("User already exist username:{} ".format(username))



records = cursor.execute("SELECT * FROM users").fetchall()
for record in records:
    print(record)
