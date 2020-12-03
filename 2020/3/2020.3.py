import os
import re


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
        if xpos >= len(row) - 1:
            xpos -= len(row) - 1
        print(row, end='')
    print(f"\nTree count: {treeCount}")
    return treeCount

def parse_map(lines):
    mapArray = []
    for line in lines:
        mapArray.insert(line)
    return mapArray

def read_file():
    file = os.path.join(os.path.dirname(__file__), 'input.txt')
    lines = ''
    values = set()
    with open(file, 'r') as file:
        lines = file.readlines()
    slope1 = part1(lines, 1, 1)
    slope2 = part1(lines, 3, 1) # part 1 answer
    slope3 = part1(lines, 5, 1)
    slope4 = part1(lines, 7, 1)
    slope5 = part1(lines, 1, 2)

    print(f"{slope1} * {slope2} * {slope3} * {slope4} * {slope5} = {slope1 * slope2 * slope3 * slope4 * slope5}")

# clean this up later
read_file()