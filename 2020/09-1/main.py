file = open('input.txt', 'r')
lines = list(file.readlines())

def testXmas(index):
    currentNum = int(lines[index])
    for j in range(i-24, i):
        for k in range(index-25, j):
            if(int(lines[j]) + int(lines[k]) == currentNum):
                return True
    return False


for i in range(25, len(lines)):
    if(not testXmas(i)):
        print(lines[i])