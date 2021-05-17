import datetime
import pickle
import operator
import dill

class Book:
    ISBN: int
    name: str
    author: str
    publisher: str
    publish_date: datetime.date

    def __init__(self, ISBN, name, author, publisher, publish_date):
        self.ISBN = ISBN
        self.name = name
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date


with open('books.pkl', 'rb') as file:
    code_unpickle = dill.load(file)
    sorted(code_unpickle, key=operator.attrgetter('ISBN'))
    sorted(code_unpickle, key=operator.attrgetter('name'))
