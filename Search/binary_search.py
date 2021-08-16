# Here we are implementing a binary search that returns the index of the target

# Binary search takes a list and target value. It will check if the middle
# value equals the target; if not the half in which the target cannot lie is
# removed and we continue this process on the remaining list. If the search
# ends with the remaining half being empty, the target is not in the array.

# This algorithm runs in O(log[n]) as for each iteration we are removing half
# the list.


def binary_search(array: list, target: int) -> bool:
    # Set our boundaries:
    left = 0
    right = len(array) - 1
    middle = int((left + right) / 2)

    # Iterate until our middle is known to not exist
    while left <= right:
        if target == array[middle]:
            print("Your target value is located at index " + str(middle))
            return True
        elif target > array[middle]:
            left = middle + 1
            middle = int((left + right) / 2)
        else:
            right = middle - 1
            middle = int((left + right) / 2)
    print("Your target value could not be located")
    return False
