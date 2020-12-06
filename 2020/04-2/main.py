import re

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

currentPassport = ''
validCount = 0

def birthYearRule(value):
    return re.match('^\d{4}$', value) and int(value) >= 1920 and int(value) <= 2002

def issueYearRule(value):
    return re.match('^\d{4}$', value) and int(value) >= 2010 and int(value) <= 2020

def expirationYearRule(value):
    return re.match('^\d{4}$', value) and int(value) >= 2020 and int(value) <= 2030

def heightRule(value):
    match = re.match('^(\d{2,3})(cm|in)$', value)
    if(match):
        heightValue = int(match.group(1))
        if(match.group(2) == 'cm'):
            return heightValue >= 150 and heightValue <= 193
        elif(match.group(2) == 'in'):
            return heightValue >= 59 and heightValue <= 76
    return False

def hairColorRule(value):
    return re.match('^#[a-f0-9]{6}$', value)

def eyeColorRule(value):
    return re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', value)

def passportIdRule(value):
    return re.match('^\d{9}$', value)

def validateFieldForRule(fieldName, value):
    fieldRules = {
        'byr': birthYearRule,
        'iyr': issueYearRule,
        'eyr': expirationYearRule,
        'hgt': heightRule,
        'hcl': hairColorRule,
        'ecl': eyeColorRule,
        'pid': passportIdRule
    }
    return fieldRules[fieldName](value)

def testForValidity(passport):
    for field in requiredFields:
        fieldIndex = passport.find(field + ':')
        if(fieldIndex == -1):
            return 0
        fieldValueStart = fieldIndex + len(field) + 1
        fieldValueEnd = passport.find(' ', fieldIndex)
        fieldValueStr = passport[fieldValueStart:fieldValueEnd]
        if(not validateFieldForRule(field,fieldValueStr)):
            return 0
    return 1

for i in range(0, len(lines)):
    if(lines[i] == '\n'):
        validCount += testForValidity(currentPassport)
        currentPassport = ''
        continue
    currentPassport += (lines[i].rstrip() + ' ')
print(validCount)