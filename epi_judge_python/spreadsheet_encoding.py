from test_framework import generic_test

import string

def ss_decode_col_id(col: str) -> int:
    col = reversed(col)
    out = 0
    for i,s in enumerate(col):
        val = string.ascii_uppercase.index(s)+1
        times = 26 ** i
        out+= val*times
    return out


if __name__ == '__main__':

    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
