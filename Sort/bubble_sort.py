from utils.helpers import swap


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
