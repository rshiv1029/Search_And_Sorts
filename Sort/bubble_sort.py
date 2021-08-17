# Here we are implementing a Bubble Sort.

# Bubble Sort is a  sorting algorithm that works by  swapping adjacent
# elements if they are in wrong order.

# The time complexity is O(n^2) as it is forced to go through every element
# and compare even if it is sorted.

from Sort.utils.helpers import swap


def bubble_sort(arr: list) -> list:
    length = len(arr)
    for iter in range(0, length):
        for i in range(0, length - 1 - iter):
            if arr[i] > arr[i + 1]:
                arr = swap(arr, i, i + 1)
            else:
                continue
    print("Sorted array is " + str(arr))
    return arr
