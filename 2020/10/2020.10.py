import os
import re
import requests
import utils
import sys


class Joltage_Adapter:    
    def __init__(self, jolt):
        self.joltage = jolt
        self.availableAdapters = set()
        self.totalPaths = -1 # Total paths from this node to zero

    def __str__(self):
        return str(self.joltage)

    def __repr__(self):
        return f"<{self.joltage}: {list(map(lambda x: str(x), self.availableAdapters))}, total: {self.totalPaths}>"


def find_adapter_zero(adapter: Joltage_Adapter, chain: list):
    if adapter.joltage == 0:
        # We did it!
        #print(list(map(lambda x: str(x), chain)))  # uncomment this if you want SPAM
        adapter.totalPaths = 1
        return 1
    else:
        # Check children adapters
        totalChildrenPaths = 0
        chain.append(adapter)
        for childAdapter in adapter.availableAdapters:
            if (childAdapter.totalPaths != -1):
                # Already calculated, let's not do it again
                totalChildrenPaths += childAdapter.totalPaths
            else:
                pathcount = find_adapter_zero(childAdapter, chain)
                totalChildrenPaths += pathcount
        adapter.totalPaths = totalChildrenPaths
        return totalChildrenPaths
            

def read_file():
    rawInput = utils.get_input("2020", "10")
    data = sorted(list(map(lambda x: int(x), rawInput.split("\n"))))

    # part 1
    previousAdapterJoltage = 0
    joltageDiffMap = {1:0, 2:0, 3:0}
    for adapterJoltage in data:
        joltageDifference = adapterJoltage - previousAdapterJoltage
        joltageDiffMap[joltageDifference] += 1
        previousAdapterJoltage = adapterJoltage

    part1Answer = joltageDiffMap[1] * (joltageDiffMap[3] + 1)
    print(f"Part 1: {part1Answer}")

    # part 2
    adapters = dict()
    outlet = Joltage_Adapter(0)
    adapters[0] = outlet

    for adapterJoltage in data:
        adapter = Joltage_Adapter(adapterJoltage)
        for availableJoltage in range(1, 4): # Up to 3 difference
            targetJoltage = adapterJoltage - availableJoltage
            if targetJoltage in data or targetJoltage == 0:
                adapter.availableAdapters.add(adapters[targetJoltage])
        adapters[adapterJoltage] = adapter

    deviceJoltage = data[-1] + 3 # Largest one + 3
    deviceAdapter = Joltage_Adapter(deviceJoltage)
    deviceAdapter.availableAdapters.add(adapters[data[-1]])
    part2Answer = find_adapter_zero(deviceAdapter, [])
    # print(adapters)
    print(f"Part 2: {part2Answer}")
    

# clean this up later
read_file()