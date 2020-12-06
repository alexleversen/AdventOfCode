import re

file = open('input.txt', 'r')
lines = list(file.readlines())

def computeId(seat):
    return 8 * seat['row'] + seat['col']

def findSeat(location, ranges):
    if(re.match('^(L|R)+$', location)):
        colDiff = int((ranges['maxCol'] - ranges['minCol'] + 1) / 2)
        if(location[0] == 'L'):
            ranges['maxCol'] -= colDiff
        else:
            ranges['minCol'] += colDiff
        if(len(location) == 1):
            return { 'row': ranges['minRow'], 'col': ranges['minCol'] }
    else:
        rowDiff = int((ranges['maxRow'] - ranges['minRow'] + 1) / 2)
        if(location[0] == 'F'):
            ranges['maxRow'] -= rowDiff
        else:
            ranges['minRow'] += rowDiff
    return findSeat(location[1:], ranges)

highestId = 0

for line in lines:
    currentId = computeId(findSeat(line.rstrip(), { 'minRow': 0, 'maxRow': 127, 'minCol': 0, 'maxCol': 7 }))
    if(currentId > highestId):
        highestId = currentId

print(highestId)