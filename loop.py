#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program does looping


def main():
    # variables
    sum = 0
    counter = 0

    # input
    number = int(input("Enter a positive integer: "))

    # process & output
    while counter <= number:
        sum = sum + counter
        counter = counter + 1
    print("The sum of all the numbers is " + str(sum) + ".")


if __name__ == "__main__":
    main()
