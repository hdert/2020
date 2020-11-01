import sqlite3
from sqlite3 import Error
import os.path


def conn_db():
    conn = None
    db_file = "main.db"

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn.cursor()


def line_print(len_id, len_username, len_score):
    spaces = 10
    print("—" * (spaces + len_id + len_username + len_score))


def show_db(c):
    c.execute("SELECT rowid,* FROM players ORDER BY score DESC")
    records = c.fetchall()
    len_score = len(str(records[0][2]))
    if len_score < 5:
        len_score = 5
    len_id = len(str(len(records)))
    if len_id < 2:
        len_id = 2
    len_username = len(records[0][1])
    for i in records:
        if len(i[1]) > len_username:
            len_username = len(i[1])
    line_print(len_id, len_username, len_score)
    print(
        f"| {'id':>{len_id}} | {'name':^{len_username}} | {'score':>{len_score}} |"
    )
    for i in records:
        print(
            f"| {i[0]:{len_id}} | {i[1]:{len_username}} | {i[2]:{len_score}} |"
        )
    line_print(len_id, len_username, len_score)


def main():
    if not os.path.isfile('main.db'):
        import dbCreate
        dbCreate.main()
    c = conn_db()
    show_db(c)


if __name__ == "__main__":
    main()
