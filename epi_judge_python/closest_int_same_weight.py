from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    # what we want to do here is basically swap the first different bits to get the same weight but closest abs val

    # to do this, we loop from 0 to 63
    for i in range(63):
        shift1 = x >> i
        shift2 = x >> i+1
        if shift1 & 1 != shift2 & 1:
            return x ^ ((1 << i) | (1 << i+1))










































    # loop through 64 bit int and compare i with i+1, if they differ, swap them
    # for i in range(63):
    #     # if differ
    #     bit1 = x >> i & 1
    #     bit2 = x >> i+1 & 1
    #     if bit1 != bit2:
    #         #swap em
    #         x ^= 1 << i | 1 << i+1
    #         break;
    # return x



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
