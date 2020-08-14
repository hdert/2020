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


def linePrint(records, unameLen):
    idLen = len(str(len(records))) + 1
    scoreLen = len(str(records[0][2])) + 3
    spaces = 10
    print("—" * (spaces + unameLen + scoreLen + idLen))


def showDb(c):
    c.execute("SELECT rowid,* FROM players ORDER BY score DESC")
    records = c.fetchall()
    linePrint(records, 7)
    print(f"|{'id':^4}|{'name':^9}|{'score':^7}|")
    for i in records:
        print('|', f"{i[0]:>2}", '|', i[1], '|',
              f"{i[2]:{len(str(records[0][2])) + 3}}", '|')
    linePrint(records, 7)


def main():
    if not os.path.isfile('main.db'):
        import dbCreate
        dbCreate.main()
    conn, c = connDb()
    showDb(c)


if __name__ == "__main__":
    main()
