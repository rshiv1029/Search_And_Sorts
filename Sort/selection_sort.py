# Here we are implementing a Selection Sort.

# Selection Sort is a sorting algorithm that works by finding the minimum
# value each iteration and adding it to the beginning of the array.

# Due to the nested loops, the time complexity is O(n^2) as it is forced to
# find the minimum every element and add to the beginning of the subarray even
# if it is sorted.

from Sort.utils.helpers import swap


def selection_sort(arr: list) -> list:
    length = len(arr)
    sub = 0
    small = sub
    while sub < length - 1:
        # Find the smallest value in the unsorted subarray
        for i in range(sub, length):
            small = i if arr[i] < arr[small] else small
        # Swap the smallest with the beginning of the unsorted array
        arr = swap(arr, sub, small)
        # Now the sorted subarray includes the beginning of the unsorted
        # subarray. The unsorted subarray now shrinks
        sub += 1
        small = sub
    print("Sorted array is " + str(arr))
    return arr
