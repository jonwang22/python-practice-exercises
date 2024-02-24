#!/bin/python3

import math
import os
import random
import re
import sys
import logging

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# s = '12:01:00PM'
# Return '12:01:00'.
#
# s = '12:01:00AM'
# Return '00:01:00'.

# How does military time work? It covers from 00:00:00 to 23:59:59 and then resets at 00:00:00 for the new day.
# AM/PM Time formate is from 12:00:00 to 11:59:59 and then flips AM and PM flag and resets to 12:00:00
# One can assume that you simply take the time and add 12 hours to get the military time 
# but this causes a problem with the clock resetting at midnight for the new day at 00:00:00 
# and it would not be 24:00:00. So our limits are the following:
# 12:00:00AM = 00:00:00, 11:59:59AM = 11:59:59, 12:00:00PM = 12:00:00, 11:59:59PM = 23:59:59
# Things this function needs to do:
# Extract the Hour and AM/PM flag from the time input. How do I split the time string?
# Read that Hour and AM/PM flag to determine if manipulation is required to convert to military time.
# The only times that need actual manipulation is 1:00PM to 12:59:59AM.
# Anytime after 1:00PM, add 12 hours to the hour to get the military time hour.
# For Midnight, 12:00AM needs to change to 00 for the hour.


def timeConversion(s):
    # To split the time string, we'll need to implement splitting string into a list
    # and using slicing to pull the necessary information of seconds and AM/PM from the last
    # element in the list. Data structure used with time split is arrays and operation used
    # array slicing.
    time_split = s.split(":")
    hours = int(time_split[0])
    minutes = int(time_split[1])
    seconds = int(time_split[2][:2])
    am_pm = time_split[2][-2:]

    # Calculating when we need to manipulate the hours based off the hours and AM/PM flag.
    if am_pm == "PM" and hours != 12:
        hours += 12
    elif am_pm == "AM" and hours == 12:
        hours = 0

    # Formatting time to military time.
    military_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    return military_time

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    print(result)