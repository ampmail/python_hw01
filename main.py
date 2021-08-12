from car import *
from book import *

if __name__ == '__main__':
    '''
    car
    '''
    # d = Dealer()
    # myCar = d.sell('red')
    # if isinstance(myCar, Car):
    #     myCar.drive()
    # else:
    #     print(myCar)

    '''
    book
    '''
    b = []
    b.append(Book('Fantasy tale', 'Fantasist Man', (1980, 10, 14), Genre.FANTASY))
    b.append(Book('History tale', 'Some Historical Man', (2000, 12, 31), Genre.HISTORY))
    b.append(Book('Poetry tale', 'Unknown Poetry', (1950, 1, 24), Genre.POETRY))
    b.append(Book('Fantasy tale', 'Fantasist Man', (1980, 10, 14), Genre.FANTASY))

    # b[0].add_annotation('cool reading')
    # b[1].add_annotation('good text')
    # b[1].add_annotation('cool text')
    # b[3].add_annotation('too boring')

    b[0].add_a('cool reading')
    b[1].add_a('good text')
    b[1].add_a('cool text')
    b[3].add_a('too boring')

    print(b)
    for book in b:
        print(book)

    # print(b[0] == b[3])
    # print(b[0] != b[3])
    # print(b[0] == b[1])
    # print(b[0] != b[1])
