import sqlite3

connection = sqlite3.connect('app.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password,
    )VALUES (
        'godlove',
        'godlove',
    );"""    
)

connection.commit()
cursor.close()
connection.close()
