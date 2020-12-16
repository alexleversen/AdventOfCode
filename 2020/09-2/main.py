file = open('input.txt', 'r')
lines = list(map(int, file.readlines()))

def testXmas(index):
    currentNum = lines[index]
    for j in range(index-24, index):
        for k in range(index-25, j):
            if(lines[j] + lines[k] == currentNum):
                return True
    return False

def getInvalidIndex():
    for i in range(25, len(lines)):
        if(not testXmas(i)):
            return i

invalidIndex = getInvalidIndex()
invalidNumber = lines[invalidIndex]

for i in range(invalidIndex):
    for j in range(i):
        rangeSum = 0
        for k in range(j,i+1):
            rangeSum += lines[k]
        if(rangeSum == invalidNumber):
            print(max(lines[j:i+1]) + min(lines[j:i+1]))
            exit(0)
