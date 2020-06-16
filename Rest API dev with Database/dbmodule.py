import sqlite3

def create_table():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    sql_create_query = 'CREATE TABLE users (id TEXT, password TEXT, phone_number TEXT)'
    cursor.execute(sql_create_query)

    conn.commit()
    conn.close()

def insert_data(id_, pass_, phone_):
    # using id_ as id is a key word in python.
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    sql_insert_query = 'INSERT INTO users values (?, ?, ?)'
    cursor.execute(sql_insert_query, (id_, pass_, phone_))

    conn.commit()
    conn.close()

def fetch_data():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    sql_select_query = 'SELECT * FROM users'
    cursor.execute(sql_select_query)
    all_users = cursor.fetchall()

    conn.close()
    return all_users

def update_password(id_, pass_):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    sql_update_query = 'UPDATE users SET password = ? where id = ?'
    cursor.execute(sql_update_query, (pass_, id_))

    conn.commit()
    conn.close()
    return 'password updated'

def fetch_user(id_, pass_):
    user = None
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    sql_select_query = 'SELECT *  FROM users WHERE id = ? and password = ?'
    cursor.execute(sql_select_query, (id_, pass_))
    user = cursor.fetchall()

    conn.commit()
    conn.close()
    return user


# create_table()
# insert_data('manoj', 'manoj', '999456781')
# print(fetch_data())
# update_password('manoj', 'manoj1234')
# print(fetch_data())
# print(fetch_user('manoj', 'manoj14'))