import re

file = open('input.txt', 'r')
lines = list(file.readlines())

rules = {}

def innerBagCount(bagType):
    innerBags = rules[bagType]
    bagCount = 0
    for bags in innerBags:
        bagCount += bags['count'] * (1 + innerBagCount(bags['type']))
    return bagCount

for line in lines:
    splitLine = line.rstrip().split(' bags contain ')
    containerBag = splitLine[0]
    containedBags = splitLine[1].split(', ')
    containedBagTypes = []
    for bag in containedBags:
        if(bag == 'no other bags.'):
            break
        bagCount, bagType = re.match('^(\d+) (.+) bags?\.?$', bag).group(1, 2)
        containedBagTypes.append({ 'type': bagType, 'count': int(bagCount) })
    rules[containerBag] = containedBagTypes

print(innerBagCount('shiny gold'))