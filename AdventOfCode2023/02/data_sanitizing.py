# https://adventofcode.com/2023/day/2
# Sanitize data into dict (games) of list (draws) of dicts (draw)
def main(raw_data):
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

    return data
