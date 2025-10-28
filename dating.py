#!/usr/bin/env python3
# Created by: Patrick
# Created on: 10/28/2025
# Can you date my grandchild program.


def main():
    # Ask user if they are rich and or good looking
    rich = input("Are you rich? yes/no: ").strip().lower()
    good_looking = input("Are you really good looking? yes/no: ").strip().lower()

    # Decide if they can date the grandchild
    if rich == "yes" or good_looking == "yes":
        print("You can date their Grandchild!")

    # If both answers are no
    elif rich == "no" or good_looking == "no":
        print("You cannot date their Grandchild.")

    # If the user inputs something other than yes or no
    else:
        print("Invalid input, please answer with 'yes' or 'no'.")


# Run the main function
if __name__ == "__main__":
    main()
