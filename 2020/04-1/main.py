file = open('input.txt', 'r')
lines = list(file.readlines())

requiredFields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]
optionalFields = [
    'cid'
]

currentPassport = ''
validCount = 0

def testForValidity(passport):
    for field in requiredFields:
        if(passport.find(field + ':') == -1):
            return 0
    return 1

for i in range(0, len(lines)):
    if(lines[i] == '\n'):
        validCount += testForValidity(currentPassport)
        currentPassport = ''
        continue
    currentPassport += (lines[i].rstrip() + ' ')
print(validCount)