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


def showDb(c):
    c.execute("SELECT * FROM players ORDER BY score DESC")
    records = c.fetchall()
    for i in records:
        print(i[0], f"{i[1]:{len(str(records[0][1]))}}")


def main():
    if not os.path.isfile('main.db'):
        import dbCreate
        dbCreate.main()
    conn, c = connDb()
    showDb(c)


if __name__ == "__main__":
    main()
