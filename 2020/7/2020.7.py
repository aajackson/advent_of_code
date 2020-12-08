import os
import re
import requests
import utils

def add_containing_bags(innerBag: str, bagBelongsTo: dict):
    if innerBag in bagBelongsTo:
        # innerBag can be put into other bags, lets get that set
        containingBags = set()
        for outerBag in bagBelongsTo[innerBag]:
            containingBags.add(outerBag)
            containingBags |= add_containing_bags(outerBag, bagBelongsTo)
        return containingBags
    else:
        # innerBag doesn't belong to any other bags, return an empty set
        return set()

def count_inner_bags(containingBag: str, bagContains: dict()):
    if len(bagContains[containingBag]) == 0:
        # this bag doesn't have any! We're done!
        return None
    else:
        # Add up all the bags this bag contains
        totalBagsDict = dict()
        for outerCount, outerBag in bagContains[containingBag]:
            outerCount = int(outerCount)
            if outerBag not in totalBagsDict:
                totalBagsDict[outerBag] = 0
            totalBagsDict[outerBag] += outerCount

            outerBagContents = count_inner_bags(outerBag, bagContains)
            if outerBagContents != None:
                # Add the bag's contents
                for innerBag, innerCount in outerBagContents.items():
                    if innerBag not in totalBagsDict:
                        totalBagsDict[innerBag] = 0
                    totalBagsDict[innerBag] += outerCount * innerCount        
        return totalBagsDict


def read_file():
    rawInput = utils.get_input("2020", "7")
    rules = rawInput.split("\n")

    # process rules into a map (directed graph?)
    bagBelongsTo = dict() # str -> set (bag name -> set of containing bags)
    bagContains = dict() # str -> list (bag name -> list of tuples (count, bagName))
    for rule in rules:
        bagMatch = re.search("([\s\w]*) bags contain", rule)
        containingBag = bagMatch.group(1)
        containsMatches = re.findall("(\d) ([\w\s]*) bags?", rule)
        if containingBag not in bagContains:
            bagContains[containingBag] = containsMatches
        for (count, innerBag) in containsMatches:
            if innerBag not in bagBelongsTo:
                bagBelongsTo[innerBag] = set()
            bagBelongsTo[innerBag].add(containingBag)

    # find the shiny gold bag contains, and their containers
    shinyBagContainers = add_containing_bags("shiny gold", bagBelongsTo)
    shinyGoldBagContainerCount = len(shinyBagContainers)
    print(f"Shiny bag containers: {shinyGoldBagContainerCount}")

    # count the number of bags inside the shiny gold bag
    shinyBagContains = count_inner_bags("shiny gold", bagContains)
    shinyBagContainsCount = 0
    for (bag, count) in shinyBagContains.items():
        shinyBagContainsCount += count
    print(f"Shiny bag contains X bags: {shinyBagContainsCount}")

# clean this up later
read_file()