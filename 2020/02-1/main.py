file = open('input.txt', 'r')
lines = file.readlines()

validCount = 0

for line in lines:
    sections = line.split(':')
    rule = sections[0]
    pwd = sections[1]
    ruleSections = rule.split(' ')
    countRange = ruleSections[0]
    letter = ruleSections[1][0]
    rangeSections = countRange.split('-')
    lower = int(rangeSections[0])
    upper = int(rangeSections[1])
    charCount = 0
    for i in range(0, len(pwd)):
        if(pwd[i] == letter):
            charCount += 1
    if(charCount >= lower and charCount <= upper):
        validCount += 1
print(validCount)