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