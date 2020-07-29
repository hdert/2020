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
    try:
        c.execute("""
        CREATE TABLE IF NOT EXISTS members (
        username TEXT,
        password TEXT
        );
        """)
    except:
        print("Error")
        return False
    return True


def showResults(results):
    for i in results:
        print(i[0], i[1], i[2])


def authenticate(results):
    global isGreen
    for x in range(3):
        username = input("Username: ").lower()
        for y in range(3):
            password = None
            for i in results:
                if username == i[1]:
                    password = authenticatePassword(i[2], password)
                    isGreen = False
                    if password == True:
                        print(
                            f"You successfully authenticated as the user {i[1]} with the id {i[0]}")
                        return [i[0], i[1]]
            if y == 2 and isGreen == False:
                print("You failed to authenticate")
                return
    print("You failed to authenticate")
    isGreen = False
    return


def authenticatePassword(user, password):
    if password == None:
        password = input("Password: ")
    if password == user:
        return True
    else:
        return password


# Main
isGreen = True

if __name__ == '__main__':

    conn = connect()
    c = conn.cursor()  # creating cursor
    isGreen = createTable(c)
    if isGreen == True:
        try:
            c.executemany("INSERT INTO members VALUES (?,?)", [
                ['bob', 'secret'], ['jones', 'notSoSecret'], ['bob', 's'], ['bob', 'se'], ['bob', 'sec'], ['bob', 'secr'], ['bob', 'secre']])
            c.execute("SELECT rowid,* FROM `members`")
        except:
            print("Error")
            isGreen = False
        if isGreen == True:
            results = c.fetchall()

            user = authenticate(results)
    conn.close()
