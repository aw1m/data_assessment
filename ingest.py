import json
import sqlite3
from datetime import datetime as dt
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
    username,given_name,family_name, profession =user.values()
    if given_name is None and family_name is  None and profession is  None:
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

print(cursor.execute("SELECT * FROM users").fetchall())




    # if cursor.fetchall()==[]:
    #     cursor.execute("SELECT count(*) FROM users WHERE username = ? and ()", [user['username']])
    #



# {
#     "username": "bd69061b-cf69-44cd-8e8b-c61c478c2d52",
#     "given-name": "CP",
#     "family-name": "Dehli",
#     "profession": "Nurse"
# },


#
#
# sqliteConnection = sqlite3.connect('data_assessment.db')
# cursor = sqliteConnection.cursor()
# print("Successfully Connected to SQLite")
# with open("model.sql")  as query:
#     cursor.executescript(query.read())
#
# sqliteConnection.commit()
# print("SQLite tables created")
#
# cursor.close()
# sqliteConnection.close()
# print("sqlite connection is closed")
#
#
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///data_assessment.db', echo=False)
# user_df.to_sql('users', con=engine,if_exists='append',index=False,index_label=True )
#
# engine.execute("SELECT * FROM users").fetchall()