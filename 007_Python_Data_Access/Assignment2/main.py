from book import Book
from base import Session
from menu import Menu
from datetime import datetime

session = Session()


def get_year():
    try:
        year = int(input('Input year: '))
        if year in range(datetime.now().year+1):
            return year
        else:
            return None
    except ValueError:
        return None


def book_from_console():
    title = input('Input title: ')
    year_ok = False
    while not year_ok:
        year = get_year()
        if year:
            year_ok = True
    return Book(title=title, year=year)


def insert_new_book(new):
    book_ok = True
    for book in session.query(Book).all():
        if book == new:
            book_ok = False
    if book_ok:
        session.add(new)
        session.commit()


def list_all_books():
    for book in session.query(Book).all():
        print(book)


def search(search_string):
    results = session.query(Book).filter(
        Book.title.ilike(f'%{search_string}%')).all()
    if results:
        for book in results:
            print(book)
    else:
        print('No book found!')


def search_by_year(year):
    results = session.query(Book).filter(Book.year == year).all()
    if results:
        for book in results:
            print(book)
    else:
        print(f'No book found from year {year}!')


def main():
    menu = Menu()
    while True:
        menu.show()
        option = menu.get_option
        if option == '1':
            list_all_books()
        elif option == '2':
            insert_new_book(book_from_console())
        elif option == '3':
            search_string = input('Enter search string: ')
            search(search_string)
        elif option == '4':
            year = get_year()
            if year:
                search_by_year(year)
        input('Press ENTER to continue...')


if __name__ == '__main__':
    main()
