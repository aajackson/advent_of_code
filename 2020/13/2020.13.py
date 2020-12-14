import os
import re
import requests
import utils
import sys
import copy
import math as m


def read_file():
    rawInput = utils.get_input("2020", "13")
    currentData = rawInput.split("\n")

    startTime = int(currentData[0])
    routes = list(map(lambda routeStr: int(routeStr), re.findall(r",?(\d+),?", currentData[1])))
    
    # Part 1 - Increment time until we find a bus route that corresponds
    # currentTime = startTime
    # firstBusRoute = 0
    # while firstBusRoute == 0:
    #     currentTime += 1 
    #     for route in routes:
    #         if (currentTime % route == 0):
    #             firstBusRoute = route
    #             break
    
    # waitTime = currentTime - startTime
    # print(f"Part 1: time = {currentTime}, bus = {firstBusRoute}, code = {firstBusRoute * waitTime}")


    # Part 2
    routeData = currentData[1].split(',')
    routeTimingDict = dict()
    for index, route in enumerate(routeData):
        if (route != 'x'):
            routeTimingDict[index] = int(route)
    
    # find the first match offset
    for (index, (offset, route)) in enumerate(routeTimingDict.items()):
        print(f"{index}: {route} offset by {offset}")


    print(f"{routeTimingDict}")


# clean this up later
read_file()
