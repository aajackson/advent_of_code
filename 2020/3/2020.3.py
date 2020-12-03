import os
import re


def part1(mapArray, xslope, yslope):
    # Go from 0,0 to 3, 1 until end of lines
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
    print(f"Tree count: {treeCount}", "")
    return treeCount



def part2(values):
    validCount = 0
    for value in values:
        match = re.match("(\d*)-(\d*) ([a-zA-Z]): ([a-zA-Z]*)", value)
        index1 = int(match.group(1))
        index2 = int(match.group(2))
        policyLetter = match.group(3)
        password = match.group(4)

        #passwordValid = re.match(f"{policyLetter}{{{lowBound},{highBound}}}", password)
        
        passwordValid = bool(password[index1 - 1] == policyLetter) ^ bool(password[index2 - 1] == policyLetter)
        if passwordValid:
            validCount += 1
            print(f"Password valid with letter {policyLetter} found at [{index1}] xor [{index2}] in {password}")
    print(f"Valid count: {validCount}")


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
    #mapArray = parse_map(lines)
    #part1(lines)        
    slope1 = part1(lines, 1, 1)
    slope2 = part1(lines, 3, 1)
    slope3 = part1(lines, 5, 1)
    slope4 = part1(lines, 7, 1)
    slope5 = part1(lines, 1, 2)

    print(f"{slope1} {slope2} {slope3} {slope4} {slope5} = {slope1 * slope2 * slope3 * slope4 * slope5}")

# clean this up later
read_file()