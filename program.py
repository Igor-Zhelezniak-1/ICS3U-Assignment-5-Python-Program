#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is math_program


def main():

    # input
    integer = input("Enter any number: ")

    # process & output
    try:
        number = int(integer)
        for loop_counter in range(0, 10):
            answer = number * loop_counter
            print("{0} x {1} = {2}".format(number, loop_counter, answer))

    except Exception:
        print("Please follow the instructions! Enter number!")
    finally:
        print("")
        print("Done")


if __name__ == "__main__":
    main()
