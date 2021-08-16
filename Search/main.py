# from constants import LINEAR_SEARCH
from helpers import user_input_formatter
from constants import INPUTS
from binary_search import binary_search
from linear_search import linear_search


def main():
    # Take user input for preferred searching algorithm; check if valid
    while True:
        search = input("Enter preferred search algorithm (L = Linear, B = Binary): ")
        if search in INPUTS:
            break
        else:
            print("Input correct searching abbreviation")

    # Take user input for array and format input from string to array[int]
    arr = input("Enter your array (Format Example: [1,2,3,4,5]): ")
    arr = user_input_formatter(arr)

    # Take user input for target
    target = input("Enter your target: ")

    # Call searching algorithm
    if search == "L":
        return linear_search(arr, int(target))
    if search == "B":
        return linear_search(arr, int(target))


if __name__ == "__main__":
    main()
