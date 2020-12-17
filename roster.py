import json
import sqlite3

def read_json(file_name):
    file = open("roster_data.json")
    file_data = json.load(file)
    return file_data


def process_data(file_content):
    db = sqlite3.connect("roster.sqlite")
    curr = db.cursor()

    curr.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;

    CREATE TABLE User (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name   TEXT UNIQUE
    );

    CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
    );

    CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
    );    
    ''')
    for item in file_content:
        print(item[0], item[1], item[2])
        name = item[0]
        course = item[1]
        role = item[2]
        curr.execute("INSERT OR IGNORE INTO User(name) VALUES(?)",(name,))
        curr.execute("SELECT id FROM User WHERE name = ?",(name,))
        user_id = curr.fetchone()[0]

        curr.execute("INSERT OR IGNORE INTO Course(title) VALUES(?)", (course,))
        curr.execute("SELECT id FROM Course WHERE title = ?", (course,))
        course_id = curr.fetchone()[0]

        curr.execute("INSERT OR IGNORE INTO Member(user_id, course_id, role) VALUES(?,?,?)", (user_id,course_id,role,))
        db.commit() 

if __name__ == '__main__':
    file_name = "roster_data.json"
    file_content = read_json(file_name)
    process_data(file_content)