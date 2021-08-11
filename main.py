from car import *
from book import *

if __name__ == '__main__':

    # d = Dealer()
    # myCar = d.sell('red')
    # if isinstance(myCar, Car):
    #     myCar.drive()
    # else:
    #     print(myCar)

    b = []
    b.append(Book('Fantasy tale', 'FANTASY MAN', date(1980, 10, 14), Genre.FANTASY))
    b.append(Book('History tale', 'HISTORY MAN', date(2000, 12, 31), Genre.HISTORY))
    b.append(Book('Poetry tale', 'POETRY WOMEN', date(1950, 1, 24), Genre.POETRY))
    b.append(Book('Fantasy tale', 'FANTASY MAN', date(1980, 10, 14), Genre.FANTASY))
    print(b)
