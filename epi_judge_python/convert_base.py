from test_framework import generic_test
import string

def int_to_string(num: int, base) -> str:
    if num == 0: return '0'

    out = []
    isNeg = True if num < 0 else False
    num = abs(num)

    while num > 0:
        cand = int(num) % base
        out.append(string.hexdigits[cand].upper())
        num //= base

    if isNeg:
        out.append('-')

    return ''.join(reversed(out))



def string_to_int(s: str, base) -> int:
    out,count,isNeg = 0,0,False

    for char in reversed(s):
        if char == '-':
            isNeg = True
        elif char != '+':
            out += string.hexdigits.index(char.lower()) * base ** count
            count += 1
    return -1 * out if isNeg else out


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    base10 = string_to_int(num_as_string, b1)
    return int_to_string(base10, b2)


if __name__ == '__main__':
    first = string_to_int('4B5C',14)
    print(first)
    # print(int_to_string(first,5))

    # print(convert_base('615',7,13))
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
