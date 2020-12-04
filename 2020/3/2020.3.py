import os
import re
import requests


def part1(mapArray, xslope, yslope):
    xpos = 0
    ypos = 0
    treeCount = 0
    for row in mapArray:
        if (ypos % yslope == 0):
            tobagganValue = row[xpos]
            if tobagganValue == '#': #tree
                treeCount += 1
                row = row[:xpos] + 'X' + row[xpos+1:]
            else:
                row = row[:xpos] + 'O' + row[xpos+1:]
            xpos += xslope
        ypos += 1
        if xpos >= len(row):
            xpos -= len(row)
        print(row)
    print(f"\nTree count: {treeCount}")
    return treeCount


def read_file():
    session = os.environ['AOC_SESSION']
    lines = requests.get('https://adventofcode.com/2020/day/3/input', cookies=dict(session=session)).text.strip().split('\n')
    slope1 = part1(lines, 1, 1)
    slope2 = part1(lines, 3, 1) # part 1 answer
    slope3 = part1(lines, 5, 1)
    slope4 = part1(lines, 7, 1)
    slope5 = part1(lines, 1, 2)

    print(f"{slope1} * {slope2} * {slope3} * {slope4} * {slope5} = {slope1 * slope2 * slope3 * slope4 * slope5}")

# clean this up later
read_file()