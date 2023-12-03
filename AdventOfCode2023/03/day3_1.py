# https://adventofcode.com/2023/day/3
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'day3.data')

with open(data_file_path, 'r') as file:
    raw_data = file.readlines()

number_with_coordinates_list = list()
symbol_coordinate_list = list()

# raw_data = [
#     '467..114..',
#     '...*......',
#     '..35..633.',
#     '......#...',
#     '617*......',
#     '.....+.58.',
#     '..592.....',
#     '......755.',
#     '...$.*....',
#     '.664.598..'
# ]

def chunking_next_element(line):
    isNumber = False
    isSymbol = False
    element = ''

    for char in line:
        if char == '.' and element == '':
            continue
        elif char == '.':
            return element

        if char.isdigit():
            if isSymbol:
                return element
            isNumber = True
            element += str(char)
        else:
            if isNumber:
                return element
            isSymbol = True
            return char
        
    return element

for row, line in enumerate(raw_data):
    number_with_coordinates_list.append(list())
    symbol_coordinate_list.append(list())
    clean_line = str(re.sub("[\n]", '', line))
    offset = 0

    while True:
        offseted_line = clean_line[offset:]
        if offseted_line == '':
            break

        element = chunking_next_element(offseted_line)
        if element == '':
            break

        element_starting_index = offseted_line.index(element) + offset

        if element.isdigit():
            number_with_coordinates_list[row].append([
                int(element),
                element_starting_index
            ])
        else:
            for i in range(len(element)):
                symbol_coordinate_list[row].append(i + element_starting_index)
                
        offset =+ element_starting_index + len(element)

sum_of_valid_numbers = 0
for row, numbers_in_row in enumerate(number_with_coordinates_list):
    for number_info in numbers_in_row:
        isValid = False
        number = int(number_info[0])
        number_starting_index = number_info[1]

        # Check before and after for adjacent symbols
        if (
            number_starting_index - 1 in symbol_coordinate_list[row] or
            number_starting_index + len(str(number)) in symbol_coordinate_list[row]
        ):
            sum_of_valid_numbers += number
            continue

        # Check above and bellow for adjacent symbols
        for i in range(len(str(number)) + 2):
            if row > 0:
                if (i + number_starting_index - 1) in symbol_coordinate_list[row - 1]:
                    isValid = True
                    break
            if row < len(number_with_coordinates_list) - 1:
                if (i + number_starting_index - 1) in symbol_coordinate_list[row + 1]:
                    isValid = True
                    break
        if isValid:
            sum_of_valid_numbers += number

print('total: %s' % sum_of_valid_numbers)
