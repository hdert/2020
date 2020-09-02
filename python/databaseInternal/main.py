import sqlite3
from sqlite3 import Error
import os.path


def connDb():
    conn = None
    db_file = "main.db"

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn, conn.cursor()


def linePrint(records, lenId, lenUsername, lenScore):
    spaces = 10
    print("—" * (spaces + lenId + lenUsername + lenScore))


def showDb(c):
    c.execute("SELECT rowid,* FROM players ORDER BY score DESC")
    records = c.fetchall()
    lenScore = len(str(records[0][2]))
    if lenScore < 5:
        lenScore = 5
    lenId = len(str(len(records)))
    if lenId < 2:
        lenId = 2
    lenUsername = len(records[0][1])
    for i in records:
        if len(i[1]) > lenUsername:
            lenUsername = len(i[1])
    linePrint(records, lenId, lenUsername, lenScore)
    print(
        f"| {'id':>{lenId}} | {'name':^{lenUsername}} | {'score':>{lenScore}} |"
    )
    for i in records:
        print(f"| {i[0]:{lenId}} | {i[1]:{lenUsername}} | {i[2]:{lenScore}} |")
    linePrint(records, lenId, lenUsername, lenScore)


def main():
    if not os.path.isfile('main.db'):
        import dbCreate
        dbCreate.main()
    conn, c = connDb()
    showDb(c)


if __name__ == "__main__":
    main()
