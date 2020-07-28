import sqlite3


def connect():
    dbName = 'database/info.db'
    conn = None
    conn = sqlite3.connect(dbName)
    return conn


def createTable(c):
    '''
    This makes a table
    params - none
    return - none
    '''
    c.execute("""
    CREATE TABLE IF NOT EXISTS members(
    username DATATYPE text,
    password DATATYPE text
    )
    """)


def showResults(results):
    for i in results:
        print(i[0], i[1])


def checkUser(results):
    username = input("Username: ").lower()
    for y in range(0, 3):
        password = False
        for i in results:
            if username == i[0]:
                password = checkPassword(i, password)
                if password == True:
                    return [False, i]
    return [password, False]


def checkPassword(results, password):
    if password == False:
        password = input("Password: ")
    if password == results[1]:
        return True
    else:
        return password

# Main


if __name__ == '__main__':

    conn = connect()
    c = conn.cursor()  # creating cursor
    createTable(c)
    try:
        c.executemany("INSERT INTO `members` VALUES (?,?)", [
                      ['bob', 'secret'], ['jones', 'notSoSecret'], ['bob', 's'], ['bob', 'se'], ['bob', 'sec'], ['bob', 'secr'], ['bob', 'secre']])
        c.execute("SELECT * FROM `members`")
    except:
        print("Error")

    results = c.fetchall()

    for x in range(0, 3):
        user = checkUser(results)
        if user[1] != False:
            print(
                f"You succesfully authenticated as the user {user[1][0]} {user[1][1]}")
            break
        elif x == 2 or user[0] != False:
            print("You failed to authenticate")
            break
    showResults(results)

    conn.close()
