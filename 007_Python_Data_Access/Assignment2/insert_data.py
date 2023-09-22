from base import Base, Session, engine
from book import Book

Base.metadata.create_all(engine)

session = Session()

book_1 = Book('Great Expectations', 1881)
book_2 = Book('Pride and Prejudice', 1918)
book_3 = Book('Alice\'s Adventures in Wonderland', 1920)
book_4 = Book('The Cricket on the Hearth', 2007)
book_5 = Book('Masonry: Beyond the Light', 2011)
book_6 = Book('A Short History of Nearly Everything', 2003)

session.add(book_1)
session.add(book_2)
session.add(book_3)
session.add(book_4)
session.add(book_5)
session.add(book_6)

session.commit()
session.close()
