# Name: Adventskalender-6
# Description: Caluculates the sum of different answers in travel forms for each group
# Author: DevOFVictory
# Date: 2020/12/07

# Reading inputs
print('Reading inputs...')
file = open('input.txt')
lines = file.read()
file.close()

groupAnwsers = lines.split('\n\n')

counter = 0

groupCounter = 1

# Loop through all groups and count amount of different anwers for each one
for group in groupAnwsers:
    anwers = []

    for person in group.split('\n'):
        for answer in person:
            if answer not in anwers:
                anwers.append(answer)
    counter += len(anwers)
    print('Counted', len(anwers), 'different anwers in group', groupCounter)
    groupCounter += 1

print('')
print('===========================================')
print('\033[94m\033[1m[DONE] \033[92mThe sum of different anwers of each group is:\033[4m',counter,'\033[0m')
print('===========================================')
