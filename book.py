from datetime import date
from enum import Enum


class Genre(Enum):
    POETRY = 1
    HISTORY = 2
    FANTASY = 3

    def __str__(self):
        return self.name


class Book:
    _author = str
    _name = str
    _date = date
    _genre = Genre

    def __init__(self, author, name, dt, genre):
        self._author = author
        self._name = name
        self._date = dt
        self._genre = genre

    def __repr__(self):
        return '{} / {} / {} / {}'.format(self._author, self._name, self._date, self._genre)

    def __str__(self):
        return 'Author: {} \nName: {} \nDate: {} \nGenre: {}'.format(self._author, self._name, self._date, self._genre)

