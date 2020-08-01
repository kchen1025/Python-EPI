from test_framework import generic_test

def reverse_bits(x: int) -> int:
    # loop from front and back
    # if not same, swap bits
    low,high = 0,63

    while low < high:
        bit1 = 1 & (x >> high)
        bit2 = 1 & (x >> low)

        if bit1 != bit2:
            x ^= ((1 << high) | (1 << low))

        high-=1
        low +=1

    return x

def reverse_bits_cached











































# def reverse_bits(x: int) -> int:
#     result = 0
#     i = 0
#
#     while x:
#         temp = x & 1
#         result |= (1 << (63 - i)) if temp == 1 else (0 << (63 - i))
#
#         x >>= 1
#         i+=1
#
#     return result
#
# def reverse_bits(x: int) -> int:
#     result = 0
#     i = 0
#
#     while x:
#         temp = x & 1
#         result |= (1 << (63 - i)) if temp == 1 else (0 << (63 - i))
#
#         x >>= 1
#         i+=1
#
#     return (result >> 48) & 0xFFFF
#
# PRECOMPUTED_REVERSE = [None] * 65536
# # calculate all values till for 16 bits in cache lookup
# for i in range(len(PRECOMPUTED_REVERSE)):
#     PRECOMPUTED_REVERSE[i] = reverse_bits(i)
#
# def reverse_bits_cached(x):
#     mask_size = 16
#     mask = 0xFFFF
#     return PRECOMPUTED_REVERSE[x & mask] << (3 * mask_size) | PRECOMPUTED_REVERSE[x >> mask_size & mask] << (2 * mask_size) | PRECOMPUTED_REVERSE[x >> (2*mask_size) & mask] << (mask_size) | PRECOMPUTED_REVERSE[x >> (3*mask_size) & mask]

if __name__ == '__main__':
    print(reverse_bits(5))
    # print(reverse_bits_cached(5))
    # print(reverse_bits_cached(1351510410656)) #405942121183313920
    # print((reverse_bits_cached(9223512776490647552))) # 64 bits 1 at the start of every 16

    # print(bin(65535))
    # print(bin(PRECOMPUTED_REVERSE[65535]))


    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
