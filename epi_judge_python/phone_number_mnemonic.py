from typing import List

from test_framework import generic_test, test_utils

lettersConst = [['0'],['1'],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]

def phone_mnemonic(phone: str) -> List[str]:
    output = []
    def generate(phone, startIdx, buff):
    
        if startIdx >= len(phone):
            output.append(''.join(buff))
            return

        letters = lettersConst[int(phone[startIdx])]
        if not letters: generate(phone, startIdx+1, buff)

        for char in letters:
            buff.append(char)
            generate(phone, startIdx+1, buff)
            buff.pop()

    generate(phone, 0, [])
    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
