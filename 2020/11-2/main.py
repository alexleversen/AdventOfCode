file = open('input.txt', 'r')
currentState = list(map(lambda value: value.rstrip(), file.readlines()))
height = len(currentState)
width = len(currentState[0])

nextState = []

def isNeighborOccupied(xPoint, yPoint, xDir, yDir):
    newXPoint = xPoint + xDir
    newYPoint = yPoint + yDir
    if(newXPoint < 0 or newXPoint >= width or newYPoint < 0 or newYPoint >= height):
        return False
    pointValue = currentState[newYPoint][newXPoint]
    if(pointValue == '.'):
        return isNeighborOccupied(newXPoint, newYPoint, xDir, yDir)    
    return pointValue == '#'

def transition(x, y):
    neighborCount = 0
    for [xDir, yDir] in [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]:
        if(isNeighborOccupied(x, y, xDir, yDir)):
            neighborCount += 1
    if(currentState[y][x] == 'L' and neighborCount == 0):
        return '#'
    if(currentState[y][x] == '#' and neighborCount >= 5):
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