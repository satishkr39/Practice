import sqlite3


def read_text_file(file_name):
    file_handle = open(file_name)
    return file_handle


def process_data(file_handle):
    conn = sqlite3.connect("week2.sqlite")
    print(sqlite3.version)
    curr = conn.cursor()
    curr.execute('''DROP TABLE IF EXISTS Counts''')
    curr.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')
    for row in file_handle:
        if not row.startswith('From: '): continue
        print(row)
        org_name = row.split(" ")[1].split("@")[1]
        print(org_name)
        curr.execute("SELECT count FROM Counts WHERE org = ?",(org_name,))
        org_exits = curr.fetchone()
        print(org_exits)
        if org_exits is None:
            curr.execute("INSERT INTO Counts (org,count) VALUES(?,1)",(org_name,))
        else:
            curr.execute("UPDATE Counts SET count=count+1 WHERE org= ?",(org_name,))
        conn.commit()


if __name__ == '__main__':
    #file_name = input("Enter file name")
    file_handle = read_text_file("mbox.txt")

    process_data(file_handle)