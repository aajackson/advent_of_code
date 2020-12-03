import os
import re


def part1(values):
    validCount = 0
    for value in values:
        match = re.match("(\d*)-(\d*) ([a-zA-Z]): ([a-zA-Z]*)", value)
        lowBound = int(match.group(1))
        highBound = int(match.group(2))
        policyLetter = match.group(3)
        password = match.group(4)

        #passwordValid = re.match(f"{policyLetter}{{{lowBound},{highBound}}}", password)
        policyLetterCount = password.count(policyLetter)
        passwordValid = lowBound <= policyLetterCount and policyLetterCount <= highBound
        if passwordValid:
            validCount += 1
            print(f"Valid: {lowBound} to {highBound} has {password} with {policyLetter}")
    print(f"Valid count: {validCount}")


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


def read_file():
    file = os.path.join(os.path.dirname(__file__), 'input.txt')
    lines = ''
    values = set()
    with open(file, 'r') as file:
        lines = file.readlines()
    
        
    
    #part1(lines)
    part2(lines)
    
    


# clean this up later
read_file()