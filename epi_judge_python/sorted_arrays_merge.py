from typing import List

from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    heap,iters,out = [],[],[]
    # create initial heap with vals and iterators
    for i,arr in enumerate(sorted_arrays):
        arrIter = iter(arr)
        nextVal = next(arrIter, None)

        iters.append(arrIter)
        if nextVal != None:
            heapq.heappush(heap, (nextVal, i))


    while heap:
        currVal, currIterIdx = heapq.heappop(heap)
        out.append(currVal)

        nextVal = next(iters[currIterIdx], None)
        if nextVal != None:
            heapq.heappush(heap, (nextVal, currIterIdx))

    return out






if __name__ == '__main__':
    # print(merge_sorted_arrays([[1,2,3],[2,5,6],[3,8,9]]))

    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
