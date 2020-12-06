import os
import re
import requests
import utils


def read_file():
    rawInput = utils.get_input("2020", "6")
    groups = rawInput.split("\n\n")
    
    # part 1
    sumGroups = 0
    for group in groups:
        groupAnswers = set()
        for answer in group:
            groupAnswers.add(answer)
            if ("\n" in groupAnswers):
                groupAnswers.remove("\n")
        sumGroups += len(groupAnswers)

    print(f"Sum: {sumGroups}")

    # part 2
    totalGroups = 0
    for group in groups:
        group = group.strip()
        maxCount = group.count("\n") + 1
        #group = sorted(group.replace("\n", ""))
        
        answerCount = 0
        groupAnswers = dict()
        for answer in group:
            if answer not in groupAnswers:
                groupAnswers[answer] = 0
            groupAnswers[answer] = groupAnswers[answer] + 1
        for question, count in groupAnswers.items():
            if count == maxCount and question != "\n":
                answerCount += 1
        totalGroups += answerCount
        #print(f"Group:\n{group}\nCount: {answerCount}\n")
    
    print(f"Total: {totalGroups}")


# clean this up later
read_file()