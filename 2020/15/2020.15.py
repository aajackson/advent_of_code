import copy
import math as m
import os
import re
import sys
from collections import namedtuple

import requests
import utils

LOG_ENABLED = False

def log(statement, end='\n'):
    if LOG_ENABLED:
        print(statement, end=end)

def main():
    rawInput = utils.get_input("2020", "15")
    currentData = rawInput.split(",")

    EntryInfo = namedtuple('EntryInfo', ["timesSpoken", "lastTurnSpoken"])
    numberInfoDict = dict() # [number] -> (timesSpoken, lastTurnSpoken)
    for i, number in enumerate(currentData[:-1]):
        numberInfo = EntryInfo(1, i + 1)
        numberInfoDict[int(number)] = numberInfo
        log(f"{i + 1:3}: Start {numberInfo} Speaking {number:3}")
        pass

    lastNumberSpoken = int(currentData[-1])
    turnCount = len(currentData) + 1 
    while turnCount <= 30000000:
        # process the last spoken number
        log(f"{turnCount:3}: Processing {lastNumberSpoken:3} - ", end='')
        if lastNumberSpoken not in numberInfoDict:
            # first time spoken
            numberInfo = EntryInfo(1, turnCount - 1)
            numberInfoDict[lastNumberSpoken] = numberInfo
            lastNumberSpoken = 0 
            log(f"  New {numberInfo} Speaking   0")
        else:
            # spoken before, when?
            numberInfo = numberInfoDict[lastNumberSpoken]
            diff = turnCount - 1 - numberInfo.lastTurnSpoken
            numberInfoDict[lastNumberSpoken] = EntryInfo(numberInfo.timesSpoken + 1, turnCount - 1)
            lastNumberSpoken = diff
            log(f"Found {numberInfo} Speaking {diff:3}")
        turnCount += 1

        if (turnCount == 2020):
            print(f"Part 1 - 2020th: {lastNumberSpoken}")
        pass

    print(f"Part 2 - 30000000th: {lastNumberSpoken}")


if __name__ == "__main__":
    main()
