from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    out = []

    for i in range(1,len(s) - 2):
        if oob(s[0:i]): continue

        for j in range(i+1,len(s) - 1):
            if oob(s[i:j]): continue

            for k in range(j+1, len(s)):
                if oob(s[j:k]) or oob(s[k:]): continue

                out.append(f'{s[0:i]}.{s[i:j]}.{s[j:k]}.{s[k:]}')
    return out

def oob(s):
    if s[0] == '0' and len(s) > 1:
        return True

    if 0 > int(s) or int(s) > 255: return True
    return False


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':


    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
