import sqlite3
from sqlite3 import Error


def main():
    conn = None
    db_file = "main.db"

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS players (
        username DATATYPE text,
        score DATATYPE text
    )''')

    c.executemany("INSERT INTO players VALUES(?,?)", [['player1', 10], [
                  'player2', 20], ['player3', 5], ['player4', 15]])
    c.execute("SELECT * FROM players")
    print(c.fetchall())
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
