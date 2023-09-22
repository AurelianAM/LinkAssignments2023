import sqlite3

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title TEXT, 
                    year INT)""")
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    return conn

def insert_book(conn, book):
    query = """INSERT INTO Books (title, year) VALUES (?, ?)"""
    cursor = conn.cursor()
    bookList = cursor.execute("""SELECT * FROM Books""").fetchall()
    exists = False
    for el in bookList:
        if el[1] == book[0] and el[2] == book[1]:
            exists = True
    if not exists:
        cursor.execute(query, book)
        conn.commit()
    else:
        print('Book already exists in the database')

def show_all_books(conn):
    cursor = conn.cursor()
    bookList = cursor.execute("""SELECT * FROM Books""").fetchall()
    print('--- BOOKS ---')
    for book in bookList:
        print(f'{book[0]}. {book[1]}, {book[2]}')
    input('-------------\npress any key...')
    
def menu(conn):
    options = {
        '1' : 'Add a book',
        '2' : 'Show all books',
        'X' : 'Exit'
    }
    print('\nMENU:')
    for opt in options:
        print(f'{opt}. {options[opt]}')
    choice = input('Choose an option: ')
    if choice == '1':
        title = input('Enter the new book\'s title: ')
        try:
            year = int(input('Enter the year for the book: '))
        except ValueError:
            year = None
        insert_book(conn, (title, year))
        return True
    elif choice == '2':
        show_all_books(conn)
        return True
    else:
        return False

def main():
    database = 'library.db'
    conn = create_connection(database)

    b1 = ('Dracula', 1987)
    b2 = ('Breakfast of champions', 1973)

    with conn:
        while menu(conn):
            pass

if __name__ == '__main__':
    main()