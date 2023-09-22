from sqlalchemy import Column, Integer, String
from base import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    year = Column(Integer)

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f'Title: {self.title} | Year: {self.year}.'

    def __eq__(self, other):
        return (self.title + str(self.year)) == (other.title + str(other.year))
