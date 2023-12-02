# https://adventofcode.com/2023/day/2
import os
from data_sanitizing import main as data_sanitizing

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
data = data_sanitizing(raw_data)

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
