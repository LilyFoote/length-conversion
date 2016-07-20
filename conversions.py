from enum import Enum


class Lengths(Enum):
    METRE = 1, 'm'
    YARD = 1.094, 'yd'
    INCH = 39.37, 'in'

    def __init__(self, conversion_factor, short_string):
        self.conversion_factor = conversion_factor
        self.short_string = short_string


class Length:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return '{} {}'.format(self.value, self.unit.short_string)
