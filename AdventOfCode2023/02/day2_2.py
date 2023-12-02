# https://adventofcode.com/2023/day/2#part2
from data_sanitizing import main as data_sanitizing

# Sanitize data into dict (games) of list (draws) of dicts (draw)
data = data_sanitizing()

# Find minimum value possible by game depending on draws,
# Multiply all values,
# Add result for all games

result = 0
def reset_minimum_set():
    return {
        'red': 0,
        'blue': 0,
        'green': 0
    }

for game_number, game in data.items():
    minimum_set = reset_minimum_set()
    for draw in game:
        for color, value in draw.items():
            if value > minimum_set[color]:
                minimum_set[color] = value

    product_of_all_values_of_minimum_set = 1
    for value in minimum_set.values():
        if value == 0:
            continue
        product_of_all_values_of_minimum_set *= value
    result += product_of_all_values_of_minimum_set

print(result)
