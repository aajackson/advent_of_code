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
            if  searchY != currentY and searchX != currentX:
                continue

            if currentData[searchY][searchX] == '#': # Occupied
                occupiedCount += 1
                if occupiedCount >= 4:
                    return True
    return False


def can_occupy(currentData, currentX, currentY):
    maxY = len(currentData)
    maxX = len(currentData[0])

    for searchY in range(currentY - 1, currentY + 2):
        if searchY < 0 or searchY >= maxY:
            continue

        for searchX in range(currentX - 1, currentX + 2):
            if searchX < 0 or searchX >= maxX:
                continue
            if searchY != currentY and searchX != currentX:
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
    print(f"Sum: {sum}")
    return sum


def read_file():
    rawInput = utils.get_input("2020", "11")
    currentData = rawInput.split("\n")

    # part 1
    nextData = step_data(currentData)
    currentStep = 1
    while currentData != nextData:
        #print(f"\nStep {currentStep}")
        #print_data(currentData)
        currentData = copy.deepcopy(nextData)
        nextData = step_data(nextData)
        currentStep += 1
    occupiedSeats = count_data(nextData) #sum([i.count("#") for i in [row for row in nextData]])
    print(f"Part 1: {currentStep} -> {occupiedSeats}")

    

# clean this up later
read_file()