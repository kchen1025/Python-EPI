from test_framework import generic_test

from collections import defaultdict

def look_and_say(n: int) -> str:
    num = '1'
    numSwap = ''

    for i in range(n-1):
        p1,p2,count = 0,0,0

        while p2 < len(num):
            while p2 < len(num) and num[p1] == num[p2]:
                count += 1
                p2 += 1
            numSwap += f'{count}{num[p1]}'
            p1=p2
            count=0

        num = numSwap
        numSwap=''


    return num

if __name__ == '__main__':
    # print(look_and_say(5))
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
