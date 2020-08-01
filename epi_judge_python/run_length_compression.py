from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    num,out = 0, ''

    for i,char in enumerate(s):
        if char.isnumeric():
            num = num*10 + int(char)
        else:
            out += char*num
            num = 0
    return out


def encoding(s: str) -> str:
    if len(s)==0: return s

    mem,count,out = s[0],1,''

    for i in range(1, len(s)):
        if mem != s[i]:
            out += f'{count}{mem}'
            mem = s[i]
            count = 1
        else:
            count+=1
    out+=f'{count}{mem}'
    return out


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    
    exit(
    generic_test.generic_test_main('run_length_compression.py',
                                   'run_length_compression.tsv',
                                   rle_tester))
