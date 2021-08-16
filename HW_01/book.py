from datetime import date
from enum import Enum


class Genre(Enum):
    POETRY = 1
    HISTORY = 2
    FANTASY = 3

    def __str__(self):
        return self.name


class Annotation:
    _text = str

    def __init__(self, text):
        self._text = text

    def __repr__(self):
        return self._text

    def __str__(self):
        return self._text


class Book:
    _author = str
    _name = str
    _date = date
    _genre = Genre
    _annotation = []

    def __init__(self, name, author, set_date, genre):
        self._author = author
        self._name = name
        self._date = date(*set_date)
        self._genre = genre
        self._annotation = []

    def __eq__(self, other):
        if isinstance(other, Book):
            return self._author == other._author and \
                   self._name == other._name and \
                   self._genre == other._genre and \
                   self._date == other._date
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Book):
            return self._author != other._author or \
                   self._name != other._name or \
                   self._genre != other._genre or \
                   self._date != other._date
        return NotImplemented

    def __repr__(self):
        return '{} / {} / {} / {} > {}'.format(self._author, self._name, self._date.year, self._genre, self._annotation)

    def __str__(self):
        a = ''
        if len(self._annotation) > 0:
            a = '> ' + '\n> '.join(map(str, self._annotation)) + '\n'
        return 'Author: {} \nName: {} \nDate: {} \nGenre: {}\n{}'.format(self._author, self._name, self._date.year,
                                                                         self._genre, a)

    def add_annotation(self, text):
        self._annotation.append(Annotation(text))
