file = open('input.txt', 'r')
lines = list(map(int, file.readlines()))
lines.sort()

combinations = 1

def solveSection(start, end):
    if(end - start == 0 or end - start == 1):
        return 1
    else:
        # ??

previousIndex = 0
answer = 1

for i in range(len(lines)):
    if(i == len(lines) - 1 or lines[i + 1] - lines[i] == 3):
        answer *= solveSection(previousIndex, i)
        previousIndex = i + 1

print(answer)