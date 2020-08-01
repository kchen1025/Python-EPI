from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(num: int) -> str:
    isNeg = True if num < 0 else False
    num = abs(num)
    if num == 0: return '0'
    out = ''

    while num != 0:
        out += str(num % 10)
        num //= 10

    return '-' + out[::-1] if isNeg else out[::-1]



def string_to_int(s: str) -> int:
    if not s: return 0
    isNeg = False

    if s[0] == '-':
        isNeg = True
        s = s[1:]
    if s[0] == '+':
        s = s[1:]
    out = 0
    base = 1
    for i in reversed(s):
        out += (base * int(i))
        base *= 10
    return out if isNeg == False else out * -1

def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    print(string_to_int(int_to_string(-99999)))
    #
    # print(string_to_int('-1234'))
