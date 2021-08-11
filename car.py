class Car:

    def __init__(self, color):
        self.color = color

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.color == other.color
        return NotImplemented

    def __str__(self):
        return self.color

    def drive(self):
        print(f'Lets drive the {self.color} car!')


class Dealer:
    # Single responsibility... yeap! =)
    cars = []

    def __init__(self):
        self.cars.append(Car('red'))
        self.cars.append(Car('green'))
        self.cars.append(Car('blue'))

    def sell(self, color):
        findMyCar = Car(color)
        try:
            place = self.cars.index(findMyCar)
        except ValueError:
            place = -1

        if place >= 0:
            newCar = self.cars.pop(place)
        else:
            newCar = 'Sorry, dealer have not such car!'

        return newCar
