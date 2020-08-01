from typing import List

from test_framework import generic_test

import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, arr: List[int]) -> int:
    targetIdx = len(arr) - k

    def findHelper(start, end):
        randomIndex = random.randint(start,end)
        pivotIndex = partition(arr, start, end, randomIndex)

        # now that we have our pivot, begin comparing
        if targetIdx == pivotIndex:
            return arr[targetIdx]

        if targetIdx < pivotIndex:
            return findHelper(start,pivotIndex-1)
        else:
            return findHelper(pivotIndex+1,end)

    def partition(arr, start, end, pivotIndex):
        # swap pivotIndex with start
        arr[start],arr[pivotIndex] = arr[pivotIndex],arr[start]
        front = start+1

        # loop through the rest of the vals, if less than pivot, stay, if greatere swap to back?
        for i in range(start+1, end+1):
            # if val is greater than piv, swap with front
            if arr[i] < arr[start]:
                arr[i],arr[front] = arr[front],arr[i]
                front+=1

        # swap back pivot
        arr[front-1],arr[start] = arr[start],arr[front-1]
        return front-1

    return findHelper(0,len(arr)-1)



if __name__ == '__main__':
    # print(find_kth_largest(1,[1000]))
    # print(find_kth_largest(1,[-1,3,5,2,40,1]))
    # print(find_kth_largest(2,[-1,3,5,2,40,1]))
    # print(find_kth_largest(3,[-1,3,5,2,40,1]))
    # print(find_kth_largest(4,[-1,3,5,2,40,1]))
    # print(find_kth_largest(5,[-1,3,5,2,40,1]))
    # print(find_kth_largest(6,[-1,3,5,2,40,1]))
    # print(sorted([-1,3,5,2,40,1]))


    a = [-53, 0, 44, 16, 144, 38, -42, 125, -164, -34, -121, -22, 53, 51, 141, 52, -152, -103, 128, -146, 8, 129, 60, 61, 161, -133, -157, -128, -33, 55, 40, -163, -156, 66, -86, -118, 122, 112, 127, 93, 9, -125, -122, 105, -153, -127, 160, 63, 159, 69, -93, -6, -98, -35, -159, 85, -139, 4, -30, 17, -56, -78, 83, -8, 116, 45, -31, -26, 99, 57, -129, -16, -145, 143, 154, -62, 124, 103, -11, 86, 158, 117, -115, -107, -102, -166, 3, 132, 95, 164, 10, -41, -143, 102, 5, 84, 113, 78, -82, -90, -79, 67, -4, 24, 156, 108, 75, 145, -154, -108, 121, -148, -92, 14, -77, 27, -140, -52, 37, 106, 12, 111, -20, 42, 21, 130, -158, 72, -15, -94, 73, -147, -58, 92, -144, 30, -71, -91, 76, -45, -54, 147, 155, 96, -150, 70, 146, -69, 28, 88, 101, -123, -23, -84, 80, 139, 163, -64, -27, -55, 149, -29, 104, -44, -87, -105, -120, -142]

    print(find_kth_largest(85,a))
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
