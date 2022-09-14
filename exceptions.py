"""
Common errors - Syntax Error, TypeError, ImportError, NameError, FileNotFoundError, ValueError, IndexError, KeyError
"""

x = -5
# if x < 5:
#     raise Exception("x cannot be negative!")

# assert (x >= 0), "negative values not allowed"

try:
    # a = 5/0
    # b = 1 + '10'
    c = 10
except ZeroDivisionError as e:
    print("error")
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up')


# defining Custom Error class
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(val):
    if val > 10:
        raise ValueTooHighError('value is too high')
    if val < 5:
        raise ValueTooSmallError('value is too small', val)


# test_value(200)


try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)




