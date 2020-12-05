# Name: Adventskalender-4
# Description: Calculates the number of valid passports
# Author: DevOFVictory
# Date: 2020/12/04

# Import necessary modules
import re

# Define input
print('[INFO] Reading inputs...')
file = open('input.txt')
inputTxt = file.read()

# Define global variables
passports = []
validCounter = 0

# Bring passports into a better format -> [{'key1':'value1', 'key2':'value2'}, {'key1':'value1', 'key2':'value2'}]
print('[INFO] Formatting input...')
for p in inputTxt.split('\n\n'):
    entryArray = re.split('\n| ',p)
    entryDict = {}
    for i in entryArray:
        key = i.split(':')[0]
        value = i.split(':')[1]
        entryDict[key] = value

    passports.append(entryDict)

# Define static bounds
eyeColor = "amb blu brn gry grn hzl oth".split()
hairColors = "0123456789abcdef"

# Count how many passports are valid
print('[INFO] Start checking',len(passports),'read passports...')
for p in passports:
    if 'byr' in p and 'iyr' in p and 'eyr' in p and 'hgt' in p and 'hcl' in p and 'ecl' in p and 'pid' in p:

        print('\033[94m\033[1m[INFO] \033[93mChecking passport with id: ' + p['pid'] + '...')

        valid = False

        byr = int(p['byr'])
        iyr = int(p['iyr'])
        eyr = int(p['eyr'])
        hgt = p['hgt']
        hcl = p['hcl']
        ecl = p['ecl']
        pid = p['pid']

        hgtValid = True

        if 'cm' in hgt:
            hgt_f = int(hgt[:-2])
            if hgt_f >= 150 and hgt_f <= 193:
                hgtValid = True
            else:
                hgtValid = False
        elif 'in' in hgt:
            hgt_f = int(hgt[:-2])
            if hgt_f >= 59 and hgt_f <= 76:
                hgtValid = True
            else:
                hgtValid = False
        else:
            hgtValid = False

        if byr >= 1920 and byr <= 2002:
            if iyr >= 2010 and iyr <= 2020:
                if eyr >= 2020 and eyr <= 2030:
                    if hgtValid:
                        if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl):
                            if ecl in eyeColor:
                                if len(pid) == 9 and pid.isnumeric():
                                    validCounter += 1
                                    valid = True
        if valid:
            print('\t\033[96m-> \033[92mValid! \033[94m('+str(validCounter)+')')
        else:
            print('\t\033[96m-> \033[91mInvalid! \033[94m('+str(validCounter)+')')

print('\033[92m')
print('===========================================')
print('\033[94m\033[1m[DONE] \033[92mAmount of valid passwords:\033[4m', validCounter,'\033[0m')
print('===========================================')
