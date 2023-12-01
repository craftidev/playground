# https://adventofcode.com/2023/day/1#part2
import re

writtenDigits = {
    'zero': '0',
    'one': 'o1',
    'two': 't2',
    'three': 't3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

code = '#'

with open('day1.data', 'r') as file:
    data = file.readlines()

# Transform word into digits. Insert before to avoid the 'twone' trap
for (i, line) in enumerate(data):
    for key in writtenDigits:
        while (key in line):
            startingIndex = line.index(key)
            line = line[:startingIndex] + writtenDigits[key] + code + line[startingIndex + len(key):]
        while (code in line):
            startingIndex = line.index(code)
            line = line[:startingIndex] + key + line[startingIndex + len(code):]
        data[i] = line

# Same solution than part1 after transformation
TotalOfFirstAndLastDigitOfEachLine = 0

for line in data:
    digits = re.sub("[^\d\.]", '', line)
    TotalOfFirstAndLastDigitOfEachLine += int(digits[0] + digits[-1])

print(TotalOfFirstAndLastDigitOfEachLine)
