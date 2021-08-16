# Here we are implementing a linear search that returns the index of the target

# Linear search takes a list and target value. It will force itself through
# the list until it reaches the end. If it comes across the target value it
# will return a boolean and the index

# This algorithm runs in O(n) as we are going through each element. Thus this
# algorithm's time complexity will increase linearly as the size increases.


def linear_search(array: list, target: int) -> bool:
    for iter in range(0, len(array)):
        if array[iter] == target:
            print("Your target value is located at index " + str(iter))
            return True
    print("Your target value could not be located")
    return False
