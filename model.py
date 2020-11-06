import sqlite3

def show_age(username):

    connection = sqlite3.connect('app.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """SELECT age FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username=username))
    age = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()

    message = '{username}\'s age is {age}.'.format(username=username, age=age)
    return message 

def check_pwd(username):

    connection = sqlite3.connect('app.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(""" SELECT password FROM users WHERE username = '{username}' ORDER BY pk DESC;""".format(username=username))
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    return password


def check_users():

    connection = sqlite3.connect('app.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(""" SELECT username FROM users ORDER BY pk DESC;""")
    db_users = cursor.fetchall()
    users = []

    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()
    return users


def signup(username, password, age):

    connection = sqlite3.connect("app.db", check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(""" SELECT password FROM users WHERE username = '{username}';""".format(username=username))
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute("""INSERT INTO users(username, password, age)VALUES('{username}', '{password}', '{age}');""".format(username=username, password=password, age=age))          
        connection.commit()
        cursor.close()
        connection.close()


    else:
        return "User already exist!!!"

    return "You successfullt signed up"