import re

file = open('input.txt', 'r')
lines = list(file.readlines())

def testTermination(swapLine):
    if(lines[swapLine][0:3] == 'acc'):
        return False
    instructionIndex = 0
    instructionsVisited = []
    acc = 0

    while(True):
        if(instructionIndex == len(lines)):
            return acc
        if(instructionIndex in instructionsVisited):
            return False
        instructionsVisited.append(instructionIndex)
        match = re.match('(\w{3}) ([+-]\d+)', lines[instructionIndex])
        instruction, value = match.group(1, 2)
        if(instructionIndex == swapLine):
            if(instruction == 'jmp'):
                instruction = 'nop'
            elif(instruction == 'nop'):
                instruction = 'jmp'
        if(instruction == 'acc'):
            acc += int(value)
            instructionIndex += 1
        elif(instruction == 'jmp'):
            instructionIndex += int(value)
        else:
            instructionIndex += 1

for i in range(len(lines)):
    terminationValue = testTermination(i)
    if(terminationValue != False):
        print(terminationValue)
