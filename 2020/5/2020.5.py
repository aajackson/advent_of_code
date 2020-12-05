import os
import re
import requests
import utils


def read_file():
    rawInput = utils.get_input("2020", "5")
    seatCodes = rawInput.split("\n")
    validIds = set()
    for row in range(1, 127):
        for col in range(8):
            validIds.add(row * 8 + col)
    highestID = 0
    for seatCode in seatCodes:
        validRows = list(range(128))
        validCols = list(range(8))
        for partitionDirection in seatCode:
            if partitionDirection == 'F':
                validRows = validRows[:int(len(validRows)/2)]
            if partitionDirection == 'B':
                validRows = validRows[int(len(validRows)/2):]
            if partitionDirection == 'R':
                validCols = validCols[int(len(validCols)/2):]
            if partitionDirection == 'L':
                validCols = validCols[:int(len(validCols)/2)]
        seatId = validRows[0] * 8 + validCols[0]
        if seatId in validIds:
            validIds.remove(seatId)
        print(f"{validRows} {validCols} {seatId}")
        if seatId > highestID:
            highestID = seatId

    print(f"Highest Id: {highestID}")
    print(f"Remaining seats: {validIds}")

# clean this up later
read_file()