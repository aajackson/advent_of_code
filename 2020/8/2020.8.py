import os
import re
import requests
import utils


def process_data(data):
    # process data
    accumulator = 0
    instruction = 0
    already_ran = set()
    while instruction < len(data):
        line = data[instruction]
        already_ran.add(instruction)
        if 'acc' in line:
            accumulator += int(line[4:])
            instruction += 1
        if 'jmp' in line:
            instruction += int(line[4:])            
        if 'nop' in line:
            instruction += 1
        if instruction in already_ran:
            return False, accumulator
    return True, accumulator    


def read_file():
    rawInput = utils.get_input("2020", "8")
    data = rawInput.split("\n")

    # part 1
    _, part1Answer = process_data(data)
    print(f"Part 1: {part1Answer}")

    # part 2
    modifiedData = data
    for i in range(len(data)):
        line = modifiedData[i]
        if 'nop' in line:
            modifiedData[i] = line.replace('nop', 'jmp')
        elif 'jmp' in line:
            modifiedData[i] = line.replace('jmp', 'nop')
        terminated, accumulator = process_data(modifiedData)
        if terminated:
            print(f"Part 2: line {i}, {accumulator}")
        modifiedData[i] = line


# clean this up later
read_file()