#!/usr/bin/env python3

# Created by: Nathan Araujo
# Created on: December 13
# This program uses a random number generator
# it then calculates the average of 10 random generated numbers

import random
import constants

def main():
    # set num_of_lists to an empty list
    nums_of_list = []
    # set sum equal to 0
    sum = 0

    # For statement to loop back if the counter is between 0 and 9
    for counter in range(constants.MAX):
        random_num = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        nums_of_list.append(random_num)
        print("{} added to list at index {}".format(random_num, counter))

    # Calculate the sum of all the random generating numbers
    for counter in range(10):
        sum += nums_of_list[counter]

    # calculates the average
    average = sum / 10

    # Displaying the average
    print()
    print("The average is {}".format(average))


if __name__ == "__main__":
    main()
