import re

file = open('input.txt', 'r')
lines = list(file.readlines())

instructionIndex = 0
instructionsVisited = []
acc = 0

while(True):
    if(instructionIndex in instructionsVisited):
        break
    instructionsVisited.append(instructionIndex)
    match = re.match('(\w{3}) ([+-]\d+)', lines[instructionIndex])
    instruction, value = match.group(1, 2)
    if(instruction == 'acc'):
        acc += int(value)
        instructionIndex += 1
    elif(instruction == 'jmp'):
        instructionIndex += int(value)
    else:
        instructionIndex += 1

print(acc)