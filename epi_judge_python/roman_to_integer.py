from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    out = 0
    i = 0

    while i < len(s) - 1:
        if rom[s[i]] < rom[s[i+1]]:
            out += rom[s[i+1]] - rom[s[i]]
            i+=2
        else:
            out += rom[s[i]]
            i+=1
    if i < len(s):
        out += rom[s[i]]
    return out


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
