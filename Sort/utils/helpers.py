# Function will take user input of string in array format and convert to a
# list of ints using split function and slicing


def user_input_formatter(array: str) -> list:
    arr = array.split(",")
    arr[0] = arr[0][1:]
    arr[-1] = arr[-1][:-1]
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    return arr


def swap(arr: list, index1: int, index2: int) -> list:
    if index1 != index2:
        arr[index1] += arr[index2]
        arr[index2] = arr[index1] - arr[index2]
        arr[index1] -= arr[index2]
    return arr
