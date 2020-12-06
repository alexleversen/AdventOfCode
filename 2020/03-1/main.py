file = open('input.txt', 'r')
lines = file.readlines()

treeCount = 0
index = 0
rightSlope = 3

for line in lines:
    lineList = list(line)
    if(line[index] == '#'):
        treeCount += 1
        lineList[index] = 'X'
    else:
        lineList[index] = 'O'
    print(''.join(lineList))
    index += rightSlope
    if (index >= len(line) - 1):
        index -= (len(line) - 1)
print(treeCount)