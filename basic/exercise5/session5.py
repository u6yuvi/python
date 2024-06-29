import math
from decimal import Decimal
from fractions import Fraction

import time


def time_it(fn, *args, repetitions=1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    if not fn:
        raise TypeError("required positional argument: 'fn'")
    if not callable(fn):
        raise NameError("{fn} is not defined")
    if repetitions <= 0:
        return 0
    if not args:
        raise TypeError(f"time_it can't time {fn.__name__} function")

    # Repetition should be positive number
    total_time = []
    for _ in range(repetitions):
        start = time.perf_counter()
        fn()
        end = time.perf_counter()
        total_time.append(end - start)

    return sum(total_time) / len(total_time)


def squared_power_list(number, *args, start=0, end=5, **kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Validations "if" block
    if args:
        raise TypeError('takes maximum 1 positional arguments')

    if kwargs:
        raise TypeError('maximum 2 keyword/named arguments')
    if not number:
        raise TypeError("required positional argument: 'number'*")
    if not isinstance(number, int):
        raise TypeError("Only integer type arguments are allowed")

    if start < 0 or end < 0:
        raise ValueError("Value of start or end can't be negative")

    if end < start:
        raise ValueError("Value of start should be less than end")
    if number > 10:
        raise ValueError("Value of number should be less than 10")
    # Return the list of number to the power of numbers from start to end
    result = [pow(number, power) for power in range(start, end)]

    return result


def polygon_area(length, *args, sides=3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""

    # Validations
    if args:
        raise TypeError(
            'polygon_area function takes maximum 1 positional arguments, more provided')

    if kwargs:
        raise TypeError(
            'polygon_area function take maximum 1 keyword/named arguments, more provided')
    if not isinstance(length, float) and not isinstance(length, int):
        raise ValueError("Datatype of length should be int or float")
    if not isinstance(sides, int):
        raise ValueError("Datatype of side should be int")

    if sides < 3 or sides > 6:
        raise ValueError("Number of sides must be between 3 and 6 inclusive.")

    if sides <= 0:
        raise ValueError("Number of sides must be between 3 and 6 inclusive.")

    # Calculate the area of the regular polygon
    area = (sides * length**2) / (4 * math.tan(math.pi / sides))

    return area

    # Return area
    pass


def temp_converter(temp, *args, temp_given_in='f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    # Validations
    if args:
        raise TypeError(
            'temp_converter function takes maximum 1 positional arguments, more provided')

    if kwargs:
        raise TypeError(
            'temp_converter function take maximum 1 keyword/named arguments, more provided')
    if not isinstance(temp, float) and not isinstance(temp, int):
        raise ValueError("Datatype of temp should be int or float")

    if not isinstance(temp_given_in, str):
        raise TypeError('Charcater string expected')
    if temp_given_in.lower() not in ['c', 'f']:
        raise ValueError('Only f or c is allowed')

    if temp_given_in.lower() == 'c' and temp < -273.15:
        raise ValueError(
            "Temprature can't go below -273.15 celsius = 0 Kelvin")

    if temp_given_in.lower() == 'f' and temp < -459.67:
        raise ValueError(
            "Temprature can't go below -459.67 fahrenheit = 0 Kelvin")

    # Return the converted temprature
    if temp_given_in.lower() == 'c':
        return (temp * 9 / 5) + 32
    elif temp_given_in.lower() == 'f':
        return (temp - 32) * 5 / 9
    else:
        raise ValueError("Invalid conversion units. Please use 'c' or 'f'.")


def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    # Validations
    if not speed:
        raise TypeError("required positional argument: 'speed'")
    if not isinstance(speed, int) or isinstance(speed, float):
        raise TypeError("Speed can be int or float type only")

    if not isinstance(dist, str):
        raise TypeError("Charcater string expected for distance unit")
    if not isinstance(time, str):
        raise TypeError("Charcater string expected")

    if speed <= 0:
        raise ValueError("Speed can't be negative")
    if speed > 300000:
        raise ValueError("Speed can't be greater than speed of light")
    if args:
        raise TypeError(
            "speed_converter function takes maximum 1 positional arguments, more provided")
    if kwargs:
        raise TypeError(
            "speed_converter function take maximum 2 keyword/named arguments, more provided")

    time_map = {"ms": 60 * 60 * 1000,
                "s": 60 * 60,
                "min": 60,
                "hr": 1,
                "day": 0.0416666666666666666666666666667
                }#float(Fraction(1, 24))}

    dist_map = {
        "m": 1000,
        "km": 1,
        "ft": 3280.839895,
        "yrd": 1093.6132983377078
    }
    if dist.lower() not in dist_map:
        raise ValueError(
            "Incorrect unit of distance. Only km/m/ft/yrd allowed")

    if time.lower() not in time_map:
        raise ValueError(
            "Incorrect unit of Time. Only ms/s/min/hr/day allowed")
    dist_unit = dist_map[dist.lower()]
    time_unit = time_map[time.lower()]
    return round(speed * (dist_unit / time_unit))
