file = open('input.txt', 'r')
lines = list(file.readlines())

def createCharList():
    charList = {}
    for i in range(97, 123):
        charList[chr(i)] = 0
    return charList

charsForGroup = createCharList()
groupLength = 0
totalCount = 0

for i in range(0, len(lines)):
    if(lines[i] == '\n'):
        for j in range(97, 123):
            if(charsForGroup[chr(j)] == groupLength):
                totalCount += 1
        charsForGroup = createCharList()
        groupLength = 0
        continue
    groupLength += 1
    for char in lines[i].rstrip():
        charsForGroup[char] += 1

print(totalCount)