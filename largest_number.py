#!/usr/bin/env python3

# Created by: Donggeun Lim
# Created on: Jan 2019
# This program finds largest number

import random


def find_largest_number(random_numbers):
    # this function find the largest number in list

    largest_number = random_numbers[0]

    for counter in range(0, len(random_numbers)):
        if largest_number < random_numbers[counter]:
            largest_number = random_numbers[counter]

    return largest_number


def main():
    # this function shows the largest number in 10 random numbers

    random_numbers = []

    # input
    for loop_counter in range(1, 11):
        a_number = random.randint(1, 100)
        random_numbers.append(a_number)
        print("The random number {0} is: {1}".format(loop_counter, a_number))
    # call the funciton
    largest_number = find_largest_number(random_numbers)

    # output
    print("The largest number is: {0} ".format(largest_number))


if __name__ == "__main__":
    main()
