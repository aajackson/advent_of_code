import os
import re
import requests
import utils
import sys
import copy

def can_empty(currentData, currentX, currentY):
    maxY = len(currentData)
    maxX = len(currentData[0])
    occupiedCount = 0

    for searchY in range(currentY - 1, currentY + 2):
        if searchY < 0 or searchY >= maxY:
            continue

        for searchX in range(currentX - 1, currentX + 2):
            if searchX < 0 or searchX >= maxX:
                continue
            if  searchY == currentY and searchX == currentX:
                continue

            if currentData[searchY][searchX] == '#': # Occupied
                occupiedCount += 1
                if occupiedCount >= 4:
                    return True
    return False

def add_tuples(left: tuple, right: tuple) -> tuple:
    return tuple(map(lambda x, y: x + y, left, right)) # weird tuple math

def count_visible_occupied(currentData, currentX, currentY):
    maxY = len(currentData)
    maxX = len(currentData[0])
    occupiedCount = 0

    dirs = [(-1,-1), (0, -1), (1, -1),
            (-1, 0),          (1, 0),
            (-1, 1), (0, 1),  (1, 1)]

    def in_bounds(position: tuple) -> bool:
        return position[0] >= 0 and position[0] < maxX and position[1] >= 0 and position[1] < maxY

    for dir in dirs:
        startPos = (currentX, currentY)
        currentPos = add_tuples(startPos, dir)
        while in_bounds(currentPos):
            # Can empty a seat when 5 seats visible and occupied
            x = currentPos[0]
            y = currentPos[1]
            if currentData[y][x] == '#': # Occupied
                occupiedCount += 1
                break
            elif currentData[y][x] == 'L': # Unoccupied
                break
            currentPos = add_tuples(currentPos, dir)

    return occupiedCount


def can_occupy(currentData, currentX, currentY):
    maxY = len(currentData)
    maxX = len(currentData[0])

    for searchY in range(currentY - 1, currentY + 2):
        if searchY < 0 or searchY >= maxY:
            continue

        for searchX in range(currentX - 1, currentX + 2):
            if searchX < 0 or searchX >= maxX:
                continue
            if searchY == currentY and searchX == currentX:
                continue

            if currentData[searchY][searchX] == '#': # Occupied
                return False
    return True


def can_occupy_2(currentData, currentX, currentY):
    maxY = len(currentData)
    maxX = len(currentData[0])

    for searchY in range(currentY - 1, currentY + 2):
        if searchY < 0 or searchY >= maxY:
            continue

        for searchX in range(currentX - 1, currentX + 2):
            if searchX < 0 or searchX >= maxX:
                continue
            if searchY == currentY and searchX == currentX:
                continue

            if currentData[searchY][searchX] == '#': # Occupied
                return False
    return True


def step_data(currentData):
    maxY = len(currentData)
    maxX = len(currentData[0])
    nextData = ['.'] * len(currentData)

    for y in range(maxY):
        dataRow = currentData[y]
        nextData[y] = [char for char in dataRow]
        for x in range(maxX):
            if currentData[y][x] == 'L' and can_occupy(currentData, x, y):
                nextData[y][x] = '#'
            elif currentData[y][x] == '#' and can_empty(currentData, x, y):
                nextData[y][x] = 'L'
    return nextData


def step_data_2(currentData):
    maxY = len(currentData)
    maxX = len(currentData[0])
    nextData = ['.'] * len(currentData)

    for y in range(maxY):
        dataRow = currentData[y]
        nextData[y] = [char for char in dataRow]
        for x in range(maxX):
            occupiedCount = count_visible_occupied(currentData, x, y)
            if currentData[y][x] == 'L' and occupiedCount == 0:
                nextData[y][x] = '#'
            elif currentData[y][x] == '#' and occupiedCount >= 5:
                nextData[y][x] = 'L'
    return nextData


def print_data(data):
    for row in data:
        for char in row:
            print(char, end='')
        print()

def count_data(data):
    sum = 0
    for row in data:
        for char in row:
            if char == '#':
                sum += 1
    #print(f"Sum: {sum}")
    return sum


def read_file():
    rawInput = utils.get_input("2020", "11")
    currentData = rawInput.split("\n")

    # part 1
    nextData = step_data_2(currentData)
    currentStep = 1
    while currentData != nextData:
        print(f"nStep {currentStep} -> {count_data(nextData)}")
        #print_data(currentData)
        currentData = copy.deepcopy(nextData)
        nextData = step_data_2(nextData)
        currentStep += 1
    occupiedSeats = count_data(nextData) #sum([i.count("#") for i in [row for row in nextData]])
    print_data(currentData)
    print(f"Part 2: {currentStep} -> {occupiedSeats}")

    

# clean this up later
read_file()