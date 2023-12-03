# https://adventofcode.com/2023/day/3#part2
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'day3.data')

with open(data_file_path, 'r') as file:
    raw_data = file.readlines()

number_with_coordinates_list = list()
gear_symbol_coordinate_list = list()

raw_data = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]

def chunking_next_element(line):
    is_number = False
    element = ''

    for char in line:
        if char != '*' and not char.isdigit():
            if is_number:
                return element
            continue

        if char.isdigit():
            is_number = True
            element += str(char)
        else:
            if is_number:
                return element
            return char
        
    return element

for row, line in enumerate(raw_data):
    number_with_coordinates_list.append(list())
    gear_symbol_coordinate_list.append(list())
    clean_line = str(re.sub("[\n]", '', line))
    offset = 0

    while True:
        offseted_line = clean_line[offset:]
        if offseted_line == '':
            break

        element = chunking_next_element(offseted_line)
        if element == '':
            break
        print(element)

        element_starting_index = offseted_line.index(element) + offset

        if element.isdigit():
            number_with_coordinates_list[row].append([
                int(element),
                element_starting_index
            ])
        else:
            for i in range(len(element)):
                gear_symbol_coordinate_list[row].append(i + element_starting_index)
                
        offset =+ element_starting_index + len(element)

print(number_with_coordinates_list)
print(gear_symbol_coordinate_list)
