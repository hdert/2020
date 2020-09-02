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
        conn, c = connDb()
        c.execute('''CREATE TABLE IF NOT EXISTS players (
            username DATATYPE text,
            score DATATYPE int
        )''')

        c.executemany("INSERT INTO players VALUES(?,?)",
                      [['player1', 10], ['player2', 20], ['player3', 5],
                       ['player4', 15]])
        conn.commit()
        conn.close()


if __name__ == "__main__":
    main()
