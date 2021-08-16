import re


class Temperature:
    _temp = float

    def __init__(self, t):
        self._temp = self.validate_temp(str(t))

    def __str__(self):
        return f'{self._temp} C° & {Temperature.to_fahrenheit(self._temp)} F°'

    def __repr__(self):
        return f'{self._temp} C°'

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, t):
        self._temp = self.validate_temp(str(t))

    @property
    def temp_f(self):
        return Temperature.to_fahrenheit(self._temp)

    @temp_f.setter
    def temp_f(self, f):
        self._temp = self.validate_temp(str(f) + 'f')

    @staticmethod
    def to_celsius(f):
        if f != None:
            return round((f - 32) * 5 / 9, 1)
        else:
            print('Not valid value')

    @staticmethod
    def to_fahrenheit(c):
        if c != None:
            return round(c * 9 / 5 + 32, 1)
        else:
            print('Not valid value')

    @staticmethod
    def validate_temp(t):
        result = None
        try:
            reg = re.search(r'^-?\d+(\.\d+)*[cf]?$', t, re.IGNORECASE)
            filtered = reg.group(0)
            if 'f' in filtered.lower():
                filtered = filtered.replace('f', '')
                result = Temperature.to_celsius(float(filtered))
                print(f'Set {filtered} of Fahrenheit degree')
            else:
                filtered = filtered.replace('c', '')
                result = float(filtered)
                print(f'Set {filtered} of Celsius degree')

        except ValueError:
            print('Could not parse given value:', t)
        except AttributeError:
            print('Given line does not contain a valid temperature value:', t)

        return result
