from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    primes = [False, False] + [True] * (n-1)
    out = []

    for p in range(2,n+1):
        if primes[p]:
            out.append(p)

            for i in range(p*2, n+1, p):
                primes[i] = False
    return out





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))




























    # primes = []
    #
    # is_prime = [False,False] + [True] * (n-1)
    # for p in range(2, n+1):
    #     if is_prime[p]:
    #         primes.append(p)
    #
    #         for i in range(p*2, n+1, p):
    #             is_prime[i] = False
    # return primes
