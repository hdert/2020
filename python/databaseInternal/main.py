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


def main():
    if not os.path.isfile('main.db'):
        import dbCreate
        dbCreate.main()
    conn, c = connDb()
    c.execute("SELECT * FROM players")
    print(c.fetchall())


if __name__ == "__main__":
    main()
