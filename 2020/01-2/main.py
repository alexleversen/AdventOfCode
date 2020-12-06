file = open('input.txt', 'r')
lines = file.readlines()

numbers = list(map(int, lines))

for i, num in enumerate(numbers):
    for j in range(i, len(numbers) - 2):
        for k in range(j, len(numbers) - 1):
            if(num + numbers[j] + numbers[k] == 2020):
                print(num * numbers[j] * numbers[k])