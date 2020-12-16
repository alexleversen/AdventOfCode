file = open('input.txt', 'r')
currentState = list(map(lambda value: value.rstrip(), file.readlines()))

nextState = []

def transition(x, y):
    neighborCount = 0
    xIndices, yIndices = [], []
    if(x > 0 and x < len(currentState[y]) - 1):
        xIndices = [x-1, x, x+1]
    elif(x == 0):
        xIndices = [0, 1]
    else:
        xIndices = [len(currentState[y]) - 2, len(currentState[y]) - 1]
    if(y > 0 and y < len(currentState) - 1):
        yIndices = [y-1, y, y+1]
    elif(y == 0):
        yIndices = [0, 1]
    else:
        yIndices = [len(currentState) - 2, len(currentState) - 1]
    for xIndex in xIndices:
        for yIndex in yIndices:
            if([x,y] != [xIndex,yIndex] and currentState[yIndex][xIndex] == '#'):
                neighborCount += 1
    if(currentState[y][x] == 'L' and neighborCount == 0):
        return '#'
    if(currentState[y][x] == '#' and neighborCount >= 4):
        return 'L'
    return currentState[y][x]

occupiedCount = 0

while(True):
    hasChanged = False
    occupiedCount = 0
    for y in range(0, len(currentState)):
        nextLine = []
        for x in range(0, len(currentState[y])):
            transitionValue = transition(x, y)
            if (transitionValue != currentState[y][x]):
                hasChanged = True
            if(transitionValue == '#'):
                occupiedCount += 1
            nextLine.append(transitionValue)
        nextState.append(nextLine)
    currentState = nextState
    nextState = []
    if(not hasChanged):
        break
    
print(occupiedCount)