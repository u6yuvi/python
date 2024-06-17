from fractions import Fraction
def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    if not 2<= base <=36:
        raise ValueError("The base not in the range between 2 and 36")
    if base > len(digit_map):
        raise ValueError ("digit_map is not long enough to encode the digits")
    if len(set(digit_map)) != len(digit_map):
        raise ValueError ("Digit Map has repeating elements")
    if base < 2:
        raise ValueError('Base b must be >= 2')
#     if number < 0:
#         raise ValueError('Number n must be >= 0')
    if number == 0:
        return [0]
    digits = []
    new_n = number
    number = abs(number)
    while number > 0: 
        m = number % base 
        number = number // base # must be after modulo
        # above line can also be written as m, n = n % b, n // b
        # we have n, m = divmod(n, b)
        digits.insert(0, digit_map[m]) # insert on the left
    if new_n<0:
        return "-"+ ''.join([d for d in digits])
    if new_n>0:
        return ''.join([d for d in digits])
    return  "".join([str(i) for i in digits])


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol=1e-05
    # Check if the absolute difference is within tolerances
    diff = abs(a - b)
    return diff <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    if f_num >= 0:
        return f_num // 1
    else:
        return -(-f_num // 1)


def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    if f_num >= 0:
        return f_num // 1
    else:
        return -(-f_num // 1)
    # return f_num


def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    x = Fraction(f_num)
    if f_num>0:
        return x.numerator // x.denominator +1
    else:
        return x.numerator // x.denominator
