import os
import re
import requests
import utils
import sys
import copy
import math as m


def read_file():
    rawInput = utils.get_input("2020", "12")
    currentData = rawInput.split("\n")

    # Part 1
    shipPos = (0, 0)
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)] # i+1 = R90, E -> S -> W -> N -> E
    facing = 0
    for command in currentData:
        key = command[0]
        value = int(command[1:])
        if key == 'N':
            shipPos = utils.add_tuples(shipPos, (0, value))
        elif key == 'S':
            shipPos = utils.add_tuples(shipPos, (0, -value))
        elif key == 'E':
            shipPos = utils.add_tuples(shipPos, (value, 0))
        elif key == 'W':
            shipPos = utils.add_tuples(shipPos, (-value, 0))
        elif key == 'F':
            scaledDirection = tuple(map(lambda x: x * value, directions[facing]))
            shipPos = utils.add_tuples(shipPos, scaledDirection)
        elif key == 'R':
            facing = (facing + value // 90) % 4
        elif key == 'L':
            facing = (facing - value // 90) % 4
    
    print(f"Part 1: Pos {shipPos}, value = {abs(shipPos[0]) + abs(shipPos[1])}")

    # Part 2
    shipPos = (0, 0)
    waypointOffset = (10, 1)
    for command in currentData:
        key = command[0]
        value = int(command[1:])
        if key == 'N':
            waypointOffset = utils.add_tuples(waypointOffset, (0, value))
        elif key == 'S':
            waypointOffset = utils.add_tuples(waypointOffset, (0, -value))
        elif key == 'E':
            waypointOffset = utils.add_tuples(waypointOffset, (value, 0))
        elif key == 'W':
            waypointOffset = utils.add_tuples(waypointOffset, (-value, 0))
        elif key == 'F':
            scaledDirection = tuple(map(lambda x: x * value, waypointOffset))
            shipPos = utils.add_tuples(shipPos, scaledDirection)
        elif key == 'R':
            if value == 90:
                waypointOffset = (waypointOffset[1], -waypointOffset[0])
            elif value == 180:
                waypointOffset = (-waypointOffset[0], -waypointOffset[1])
            elif value == 270:
                waypointOffset = (-waypointOffset[1], waypointOffset[0])
        elif key == 'L':
            if value == 270:
                waypointOffset = (waypointOffset[1], -waypointOffset[0])
            elif value == 180:
                waypointOffset = (-waypointOffset[0], -waypointOffset[1])
            elif value == 90:
                waypointOffset = (-waypointOffset[1], waypointOffset[0])

    print(f"Part 2: Pos {shipPos}, value = {abs(shipPos[0]) + abs(shipPos[1])}")

# clean this up later
read_file()