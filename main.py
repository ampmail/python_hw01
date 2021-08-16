from HW_01.car import *
from HW_01.book import *
from HW_01.temp import *

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
    # b = []
    # b.append(Book('Fantasy tale', 'Fantasist Man', (1980, 10, 14), Genre.FANTASY))
    # b.append(Book('History tale', 'Some Historical Man', (2000, 12, 31), Genre.HISTORY))
    # b.append(Book('Poetry tale', 'Unknown Poetry', (1950, 1, 24), Genre.POETRY))
    # b.append(Book('Fantasy tale', 'Fantasist Man', (1980, 10, 14), Genre.FANTASY))

    # b[0].add_annotation('cool reading')
    # b[1].add_annotation('good text')
    # b[1].add_annotation('cool text')
    # b[3].add_annotation('too boring')

    # print(b)
    # for book in b:
    #     print(book)

    # print(b[0] == b[3])
    # print(b[0] != b[3])
    # print(b[0] == b[1])
    # print(b[0] != b[1])

    '''
    temperature
    '''

    # temp = '100.3c'   # str(input('Enter temperature value (with C or F postfix) > '))
    temp = -40
    t = Temperature(temp)
    print(t)
    print(f'Get in fahrenheit: {t.temp_f}')
    print(f'Get in celsius: {t.temp}')

    t.temp_f = 212
    print(f'Get in fahrenheit: {t.temp_f}')
    print(f'Get in celsius: {t.temp}')

    t.temp = '-110f'
    print(f'Get in fahrenheit: {t.temp_f}')
    print(f'Get in celsius: {t.temp}')
