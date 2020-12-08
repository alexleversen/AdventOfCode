import re

file = open('input.txt', 'r')
lines = list(file.readlines())

rules = {}

def hasShinyGoldBag(bagType):
    innerBags = rules[bagType]
    if('shiny gold' in innerBags):
        return True
    for bag in innerBags:
        if(hasShinyGoldBag(bag)):
            return True
    return False

for line in lines:
    splitLine = line.rstrip().split(' bags contain ')
    containerBag = splitLine[0]
    containedBags = splitLine[1].split(', ')
    containedBagTypes = []
    for bag in containedBags:
        if(bag == 'no other bags.'):
            break
        bagType = re.match('^\d+ (.+) bags?\.?$', bag).group(1)
        containedBagTypes.append(bagType)
    rules[containerBag] = containedBagTypes

shinyGoldBagCount = 0
count = 0

for rule in rules:
    if(hasShinyGoldBag(rule)):
        shinyGoldBagCount += 1
    count += 1
    print('checked ' + str(count) + '/' + str(len(rules)))

print(shinyGoldBagCount)