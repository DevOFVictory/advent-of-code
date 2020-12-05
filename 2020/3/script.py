# Name: Adventskalender-3
# Description: Calculates all trees, which we would encounter on the given slope
# Author: DevOFVictory
# Date: 2020/12/03

# Read Inputs
print('[INFO] Reading Input...')
file = open('input.txt')
lines = file.readlines()

# Define global variables
slope = []
output = 1

# Define different slopes
xValues = [1, 3, 5, 7, 1]
yValues = [1, 1, 1, 1, 2]

# Bring slope into a better format
for i in lines:
    slope.append(i.replace('\n', '')*100)

# Loop through all slopes and calculate the tree amount of each one
for i in range(len ( xValues ) ):
    x = 0
    y = 0
    counter = 0
    while y <= 322:
        letter = slope[y][x]
        if letter == '#':
            counter += 1
        x += xValues[i]
        y += yValues[i]
    output *= counter
    print('[INFO] Counted', counter, 'trees on the', str(i+1) + '. rope!')

# Print the total amount of trees
print('')
print('=================================================================================================')
print('[DONE] Amount of trees you would encounter on slopes muliplyed by each other:', output)
print('=================================================================================================')
