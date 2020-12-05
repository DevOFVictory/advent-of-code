# Name: Adventskalender-4
# Description: Calculates the number of valid passports
# Author: DevOFVictory
# Date: 2020/12/04

# Import necessary modules
import re

# Define input
file = open('input.txt')
inputTxt = file.read()

# Define global variables
passports = []
validCounter = 0

# Bring passports into a better format -> [{'key1':'value1', 'key2':'value2'}, {'key1':'value1', 'key2':'value2'}]
for p in inputTxt.split('\n\n'):
    entryArray = re.split('\n| ',p)
    entryDict = {}
    for i in entryArray:
        key = i.split(':')[0]
        value = i.split(':')[1]
        entryDict[key] = value

    passports.append(entryDict)

# Count how many passports are valid
for p in passports:
    if len(p) >= 7:
        if 'byr' in p and 'iyr' in p and 'eyr' in p and 'hgt' in p and 'hcl' in p and 'ecl' in p and 'pid' in p:
            validCounter += 1

print('Valid passports:',validCounter)
