# from constants import LINEAR_SEARCH
from binary_search import binary_search
from jump_search import jump_search
from linear_search import linear_search
from utils.constants import INPUTS
from utils.helpers import user_input_formatter


def main():
    # Take user input for preferred searching algorithm; check if valid
    while True:
        search = input(
            "Enter preferred search algorithm (type 'help' for list of searches): "
        )
        if search == "help":
            for alg, desc in INPUTS.items():
                print("Type '" + alg + "' for a " + desc)
        elif search in INPUTS.keys():
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
        return binary_search(arr, int(target))
    if search == "J":
        return jump_search(arr, int(target))


if __name__ == "__main__":
    main()
