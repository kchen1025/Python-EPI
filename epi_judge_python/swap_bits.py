from test_framework import generic_test


def swap_bits(x, i, j):
    # get bit at i
    i_val = x >> i & 1
    j_val = x >> j & 1

    # if equal, return x
    if i_val == j_val: return x

    # if not, create mask at i and j and return xor
    # mask = 2**i + 2**j
    mask = (i << i) | (1 << j)
    return x ^ mask





if __name__ == '__main__':
    # print(swap_bits(129, 0, 7))
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
