from bubble_sort import bubble_sort
from heap_sort import heap_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from utils.constants import INPUTS
from utils.helpers import user_input_formatter


def main():
    # Take user input for preferred searching algorithm; check if valid
    while True:
        sort = input(
            "Enter preferred search algorithm (type 'help' for list of searches): "
        )
        if sort.lower() == "help":
            for alg, desc in INPUTS.items():
                print("Type '" + alg + "' for a " + desc)
        elif sort.upper() in INPUTS.keys():
            break
        else:
            print("Input correct searching abbreviation")

    # Take user input for array and format input from string to array[int]
    arr = input("Enter your array (Format Example: [1,2,3,4,5]): ")
    arr = user_input_formatter(arr)
    sort = sort.upper()
    # Call searching algorithm
    if sort == "B":
        return bubble_sort(arr)
    # if sort == "H":
    #     return heap_sort(arr)
    if sort == "I":
        return insertion_sort(arr)
    # if sort == "M":
    #     return merge_sort(arr)
    if sort == "S":
        return selection_sort(arr)


if __name__ == "__main__":
    main()
