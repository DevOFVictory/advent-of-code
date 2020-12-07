# Name: Adventskalender-6
# Description: Caluculates the highest seat id
# Author: DevOFVictory
# Date: 2020/12/07

# Reading inputs
print('Reading inputs...')
file = open('input.txt')
lines = file.read()
file.close()

groupAnwsers = lines.split('\n\n')

alphabeth = 'abcdefghijklmnopqrstuvwxyz'

# Define Function which returns amount of characers, that are in all strings of list anwers
def getEverybodyPositives(anwers):
    amount = 0
    for letter in alphabeth:
        isInEveryone = True
        for answer in anwers:
            if letter not in answer:
                isInEveryone = False
                break
        if isInEveryone:
            amount += 1
    return amount

counter = 0

groupCounter = 1

# Loop through all groups and count amount of different anwers for each one
for group in groupAnwsers:
    answers = []

    for person in group.split('\n'):
        answers.append(person)
    counter += getEverybodyPositives(answers)
    print('Counted', getEverybodyPositives(answers), 'equal anwers in group', groupCounter)
    groupCounter += 1

print('')
print('===========================================')
print('\033[94m\033[1m[DONE] \033[92mThe sum of questions which were answered by everyone is:\033[4m',counter,'\033[0m')
print('===========================================')
