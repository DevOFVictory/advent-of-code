# Name: Adventskalender-7
# Description: Calculates the number of bags, which can contain a shiny gold bag
# Author: DevOFVictory
# Date: 2020/12/07

# Reading inputs
print('Reading inputs...')
file = open('input.txt')
lines = file.readlines()
file.close()

shinyGoldBags = []

# Seaching for start values
print('Seaching for start values...')
for rule in lines:
    if ' shiny gold bag' in rule:
        bag = rule.split(' bags')[0]
        shinyGoldBags.append(bag)
        print('Found "' + bag + '" which is containing a "shiny gold bag" at the beginning.')

print('')

# Searching for bags which can contain one of our start values
print('Starting to bruteforce potential tree... (This can take a while!)')
for shinyGoldBag in shinyGoldBags:
    for rule in lines:
        if ' ' + shinyGoldBag in rule:
            bag = rule.split(' bags')[0]
            if bag not in shinyGoldBags:
                shinyGoldBags.append(bag)
                print('Found "' + bag + '" which can contain our shiny gold bag!')

amount = len(shinyGoldBags)

# Printing output
print('')
print('===========================================')
print('\033[94m\033[1m[DONE] \033[92mThe amount of bags which can contain a "shiny gold bag" is:\033[4m',amount,'\033[0m')
print('===========================================')
