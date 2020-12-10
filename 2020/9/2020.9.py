import os
import re
import requests
import utils
import sys


def check_prev_x(arr, index, searchRange = 25):
    targetValue = arr[index]
    searchIndex = index - searchRange
    for searchValue in arr[searchIndex:index]:
        for otherValue in arr[searchIndex+1:index]:
            if searchValue + otherValue == targetValue:
                return True
    # no value found
    return False

def sum_window(arr, windowStart, windowEnd):
    sumValue = 0
    minValue = sys.maxsize
    maxValue = 0
    for value in arr[windowStart:windowEnd]:
        sumValue += value
        if minValue > value:
            minValue = value
        if maxValue < value:
            maxValue = value
    return sumValue, minValue, maxValue

def read_file():
    rawInput = utils.get_input("2020", "9")
    data = list(map(lambda x: int(x), rawInput.split("\n")))

    # process data
    # part 1
    for index in range(25, len(data)):
        if not check_prev_x(data, index):
            print(f"Value not found! {data[index]}")

    # part 2
    # create a sliding window to find the range
    # where the sum is the targetValue
    targetValue = 27911108 #from part 1
    windowStart = 0
    windowEnd = 1
    windowSum, minValue, maxValue = sum_window(data, windowStart, windowEnd)
    while windowSum != targetValue:
        if windowSum < targetValue:
            windowEnd += 1
        if windowSum > targetValue:
            windowStart += 1
        windowSum, minValue, maxValue = sum_window(data, windowStart, windowEnd)
    print(f"Window range found! [{windowStart} - {windowEnd}]. Min + max: {minValue} + {maxValue} = {minValue + maxValue}")


    

# clean this up later
read_file()