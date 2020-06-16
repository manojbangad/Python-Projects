import sqlite3

def create_table():
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS bookstore (isbn INT, title TEXT, author TEXT, year INT)')
    conn.commit()
    conn.close()

def insert_book(isbn, title, author, year):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()

    insert_query = 'INSERT INTO bookstore VALUES(?, ?, ?, ?)'
    cur.execute(insert_query, (isbn, title, author, year))

    conn.commit()
    conn.close()

def delete_book(isbn):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()

    delete_query = 'DELETE FROM bookstore where isbn = ?'
    cur.execute(delete_query, (isbn, ))

    conn.commit()
    conn.close()

def search_book(isbn = '', title = '', author = '', year = ''):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()

    search_query = 'SELECT * FROM bookstore where isbn = ? OR title = ? OR author = ? OR year = ?'
    cur.execute(search_query, (isbn, title, author, year))
    books_result = cur.fetchall()
    # print(books_result)
    conn.close()
    return  books_result

def update_data(isbn, author):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()

    update_query = 'UPDATE bookstore SET author = ? WHERE isbn = ?'
    cur.execute(update_query, (author, isbn))

    conn.commit()
    conn.close()

def get_all_books():
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()

    select_query = 'SELECT * FROM bookstore'
    # select_query = 'SELECT title FROM bookstore'
    cur.execute(select_query)
    all_books = cur.fetchall()
    # print(all_books)

    conn.commit()
    conn.close()
    return  all_books

# create_table()
# insert_book(103, 'Alchemist', 'Chetan Bhagat', 1995)
# delete_book(102)
# print(search_book(isbn = 102, year=1995))
# update_data(103, 'Polho Colioe')
print(get_all_books())