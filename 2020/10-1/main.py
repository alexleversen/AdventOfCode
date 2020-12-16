file = open('input.txt', 'r')
lines = list(map(int, file.readlines()))
lines.sort()
lines.insert(0, 0)

diffOneCount = 0
diffThreeCount = 1

for i in range(1, len(lines)):
    diff = lines[i] - lines[i-1]
    if(diff == 1):
        diffOneCount += 1
    elif(diff == 3):
        diffThreeCount += 1

print(diffOneCount * diffThreeCount)