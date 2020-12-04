import os
import re
import requests
import utils


def read_file():
    lines = utils.get_input("2020", "4")
    idArray = lines.replace("\n\n", " |").replace("\n", " ").split("|")    
    validIds = 0
    for id in idArray:
        # Quick matches!
        matches = re.findall("(iyr|byr|eyr|hgt|hcl|ecl|pid)", id)
        #validIds += 1 # part 1's answer
        # part 2
        if (len(matches) == 7):
            # Now we validate!
            byrMatch = re.search("byr:(19[2-9][0-9]|200[0-2])", id)
            iyrMatch = re.search("iyr:(201[0-9]|2020)", id)
            eyrMatch = re.search("eyr:(202[0-9]|2030)", id)
            hgtMatch = re.search("hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)", id)
            hclMatch = re.search("hcl:#([0-9|a-f]{6})\\b", id)
            eclMatch = re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)", id)
            pidMatch = re.search("pid:\\d{9}\\b", id)

            if (byrMatch and iyrMatch and eyrMatch and hgtMatch and hclMatch and eclMatch and pidMatch):
                print(id)
                validIds += 1

    print(f"Valid Ids: {validIds}")

# clean this up later
read_file()