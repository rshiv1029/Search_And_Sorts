import Search
import Sort
from constants import SEARCH, SORT
from Search.main import search_main
from Sort.main import sort_main


def main():
    # Take user input for preferred searching algorithm; check if valid
    while True:
        option = input("Enter preferred algorithm (type 'help' for list of options): ")
        if option.lower() == "help":
            print(
                "Type '"
                + SEARCH
                + "' for a Searching Algorithm \nType '"
                + SORT
                + "' for a Sorting Algorithm"
            )
        elif option.upper() == SEARCH or option.upper() == SORT:
            break
        else:
            print("Input correct algorithm")

    option = option.upper()
    # Call searching algorithm
    if option == SEARCH:
        return search_main()
    if option == SORT:
        return sort_main()


if __name__ == "__main__":
    main()
