# https://adventofcode.com/2023/day/1
import re

with open('day1.data', 'r') as file:
    data = file.readlines()

TotalOfFirstAndLastDigitOfEachLine = 0

for line in data:
    digits = re.sub("[^\d\.]", '', line)
    TotalOfFirstAndLastDigitOfEachLine += int(digits[0] + digits[-1])

print(TotalOfFirstAndLastDigitOfEachLine)
