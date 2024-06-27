import random
from decimal import *


class Qualean:
    '''
    Yous description
    '''

    def __init__(self, b=None):
        if b is not None and b not in [0, 1, -1]:
            raise ValueError("Value is not 1, 0 ,or -1")
        elif b is None:
            self.value = random.uniform(-1, 1)
            self.number = random.uniform(-1, 1)
        else:
            self.value = b * random.uniform(-1, 1)
        # self.number = *args
        # self.value = value
    # defining object representation

    def __repr__(self):
        return 'Qualean Class Instance'

    def __str__(self):
        return f'Qualean String for number: ' + str(self.number)
    # your other functions

    def return_qualean(self,):
        self.value = round(self.value, 10)
        return self.value

    def __and__(self, q2):
        if q2 is None:
            return False
        val = self.value and q2.value
        return bool(val)

    def __or__(self, q2):
        if q2 is None:
            return True
        val = self.value or q2.value
        return bool(val)

    def __add__(self, q2):
        if isinstance(q2, Qualean):
            return round(self.value, 10) + round(q2.value, 10)
        elif isinstance(q2, float):
            return round(self.value, 10) + q2
        else:
            raise TypeError("q2 is of not type Qualean")

    def __eq__(self, q2):
        if isinstance(q2, Qualean):
            return bool(self.value == q2.value)
        else:
            raise TypeError("q2 is of not type Qualean")

    def __bool__(self):
        return bool(self.value)

    def __float__(self):
        return self.value

    def __gt__(self, q2):
        if isinstance(q2, float):
            return round(self.value, 10) > q2
        if isinstance(q2, Qualean):
            return bool(self.value >= q2.value)
        else:
            raise TypeError("q2 is of not type Qualean")

    def __ge__(self, q2):
        if isinstance(q2, float):
            return round(self.value, 10) >= q2
        if isinstance(q2, Qualean):
            return bool(self.value >= q2.value)
        else:
            raise TypeError("q2 is of not type Qualean")

    def __mul__(self, q2):
        if isinstance(q2, float):
            return round(self.value, 10) * q2
        if isinstance(q2, Qualean):
            return round(self.value, 10) * round(q2.value, 10)
        else:
            raise TypeError("q2 is of not type Qualean")

    def __le__(self, q2):
        if isinstance(q2, float):
            return round(self.value, 10) <= q2
        if isinstance(q2, Qualean):
            return bool(round(self.value, 10) <= round(q2.value, 10))
        else:
            raise TypeError("q2 is of not type Qualean")

    def __lt__(self, q2):
        if isinstance(q2, float):
            return round(self.value, 10) < q2
        if isinstance(q2, Qualean):
            return bool(round(self.value, 10) < round(q2.value, 10))
        else:
            raise TypeError("q2 is of not type Qualean")

    def __invertsign__(self):
        return -round(self.value, 10)

    def __sqrt__(self):
        if self.value > 0:
            return round(Decimal(self.value).sqrt(), 10)
        return str(round(Decimal(self.value).sqrt(), 10))
