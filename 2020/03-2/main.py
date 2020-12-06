file = open('input.txt', 'r')
lines = list(file.readlines())

def treesForSlope(rightSlope, downSlope):
    index = 0
    treeCount = 0
    for i in range(0, len(lines), downSlope):
        line = lines[i]
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
    return treeCount

answer = treesForSlope(1,1) * treesForSlope(3,1) * treesForSlope(5,1) * treesForSlope(7,1) * treesForSlope(1,2)
print(answer)