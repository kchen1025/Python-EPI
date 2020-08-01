from test_framework import generic_test

def add(a,b):
    if b == 0:
        return a
    return add(a ^ b, (a & b) << 1)

def multiply(x: int, y: int) -> int:
    # multiple x by y if LSB of x is 1

    running_sum = 0
    while x:
        if x & 1 == 1:
            # add to running sum
            running_sum = add(running_sum, y)
        # shift x so we can use the next significant bit
        x >>= 1
        # shift y so we can move it over by hundreds
        y <<= 1
    return running_sum




if __name__ == '__main__':
    # print(multiply(12,12))
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
