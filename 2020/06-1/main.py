file = open('input.txt', 'r')
lines = list(file.readlines())

charsForGroup = []
totalCount = 0

for i in range(0, len(lines)):
    if(lines[i] == '\n'):
        print(charsForGroup)
        totalCount += len(charsForGroup)
        charsForGroup = []
        continue
    for char in lines[i].rstrip():
        if(not char in charsForGroup):
            charsForGroup.append(char)

print(totalCount)