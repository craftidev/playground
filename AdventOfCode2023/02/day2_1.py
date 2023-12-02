# https://adventofcode.com/2023/day/2
from data_sanitizing import main as data_sanitizing

rules = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

# Sanitize data into dict (games) of list (draws) of dicts (draw)
data = data_sanitizing()

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
