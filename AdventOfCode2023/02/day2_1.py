# https://adventofcode.com/2023/day/2
import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'day2.data')

with open(data_file_path, 'r') as file:
    raw_data = file.readlines()

rules = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

# Sanitize data into dict (games) of list (draws) of dicts (draw)
data = dict()
for line in raw_data:
    game_num_prefix = 'Game '
    game_num_start_index = line.index(game_num_prefix) + len(game_num_prefix)
    game_num_end_index = line.index(':')
    game_num = int(line[game_num_start_index:game_num_end_index])
    data[game_num] = list()

    raw_data_string = line[game_num_end_index + 1:]
    sanitized_data_string = raw_data_string.replace("\n", "")

    draw_list = sanitized_data_string.split(';')
    for draw_index, draw in enumerate(draw_list):
        data[game_num].append(dict())
        splited_draw = draw.split(' ')

        reversed_splited_draw = reversed_list = list(reversed(splited_draw))
        for element_index, element in enumerate(reversed_splited_draw):
            if element == '':
                break

            if element_index % 2 == 0:
                color = element.replace(",", "")
                continue
            else:
                value = int(element)
            
            data[game_num][draw_index][color] = value

# Add index of all possible games following the rules
result = 0
follow_rules = True
for game_number, game in data.items():
    for draw in game:
        for color, value in draw.items():
            if value > rules[color]:
                follow_rules = False
    if follow_rules == True:
        result += game_number
    follow_rules = True

print(result)
