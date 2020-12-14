import os
import re
import requests
import utils
import sys
import copy
import math as m


def mask_str(mask, value):
    maskedValue = ""
    for (i, mask_char) in enumerate(mask):
        if mask_char in ('1', '0'):
            maskedValue += mask_char
        else:
            maskedValue += value[i]
    return maskedValue


def permute_address(address):
    if 'X' in address:
        address0 = address.replace('X', '0', 1)
        address1 = address.replace('X', '1', 1)
        return [] + permute_address(address0) + permute_address(address1)
    else:
        # Already processed!
        return [address]


def mask_address(mask, address):
    processedAddress = ""
    for (i, mask_char) in enumerate(mask):
        if mask_char == '0':
            processedAddress += address[i]
        else:
            processedAddress += mask_char

    # Generate address permutations
    return permute_address(processedAddress)


def main():
    rawInput = utils.get_input("2020", "14")
    currentData = rawInput.split("\n")

    memory = dict()
    processedMemory = dict()
    # Part 1
    maskStr = ""
    for instruction in currentData:
        if 'mask' in instruction:
            maskStr = re.match(r"mask = ([X01]{36})", instruction).group(1)
        else:
            (address, decimalValue) = re.match(r"mem\[(\d+)\] = (\d+)", instruction).group(1, 2)
            memory[address] = format(int(decimalValue), "036b")
            processedMemory[address] = mask_str(maskStr, memory[address])

    processedSum = 0
    for (address, processedValue) in processedMemory.items():
        processedSum += int(processedValue, 2)

    print(f"Part 1: {processedSum}")
    

    # Part 2
    processedMemory2 = dict()
    maskStr = ""
    for instruction in currentData:
        if 'mask' in instruction:
            maskStr = re.match(r"mask = ([X01]{36})", instruction).group(1)
        else:
            (address, decimalValue) = re.match(r"mem\[(\d+)\] = (\d+)", instruction).group(1, 2)
            memoryValue = format(int(decimalValue), "036b")
            addressValue = format(int(address), "036b")
            processedAddresses = mask_address(maskStr, addressValue)
            for address in processedAddresses:
                processedMemory2[address] = memoryValue

    processedSum2 = 0
    for (address, processedValue) in processedMemory2.items():
        processedSum2 += int(processedValue, 2)
    print(f"Part 2: {processedSum2}")

if __name__ == "__main__":
    main()
