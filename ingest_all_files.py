import sqlite3
import ingest_users

sqliteConnection = sqlite3.connect('data_assessment.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")
with open("model.sql")  as query:
    cursor.executescript(query.read())
    sqliteConnection.commit()

ingest_users(cursor, sqliteConnection)



records = cursor.execute("SELECT * FROM users").fetchall()
for record in records:
    print(record)
