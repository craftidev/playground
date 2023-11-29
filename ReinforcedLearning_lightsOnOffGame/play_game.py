import numpy as np
import os

q_table_path = "q_table.npy"

if os.path.exists(q_table_path):
    loaded_q_table = np.load(q_table_path)
    loaded_q_table_list = loaded_q_table.tolist()
    print('Playing with AI help!')

def display_board(board):
    print(' ', '1', '2', '3')
    print('a', board[0], board[1], board[2])
    print('b', board[3], board[4], board[5])
    print('c', board[6], board[7], board[8])


def get_initial_board():
    board = [
        0, 1, 0,
        1, 1, 1,
        0, 1, 0
    ]
    return board


def is_board_winning(board):
    if board.count(0) == 9:
        return True
    else:
        return False


def coordinate_to_index(input_coordinate):
    index = 0

    if input_coordinate[0] == 'b':
        index = 3 + int(input_coordinate[1]) - 1
    elif input_coordinate[0] == 'c':
        index = 6 + int(input_coordinate[1]) - 1
    else:
        index = int(input_coordinate[1]) - 1

    if index >= 0 or index <= 8:
        return index
    else:
        print("Invalid move")
        return -1


def update_board(board, move_index):
    if move_index == -1:
        return board

    board[move_index] = switch_value(board[move_index])

    if move_index == 1 or move_index == 7:
        board[4] = switch_value(board[4])
        board[move_index + 1] = switch_value(board[move_index + 1])
        board[move_index - 1] = switch_value(board[move_index - 1])

    elif move_index == 3 or move_index == 5:
        board[4] = switch_value(board[4])
        board[move_index + 3] = switch_value(board[move_index + 3])
        board[move_index - 3] = switch_value(board[move_index - 3])

    elif move_index == 0:
        board[move_index + 3] = switch_value(board[move_index + 3])
        board[move_index + 1] = switch_value(board[move_index + 1])

    elif move_index == 2:
        board[move_index + 3] = switch_value(board[move_index + 3])
        board[move_index - 1] = switch_value(board[move_index - 1])

    elif move_index == 6:
        board[move_index - 3] = switch_value(board[move_index - 3])
        board[move_index + 1] = switch_value(board[move_index + 1])

    elif move_index == 8:
        board[move_index - 3] = switch_value(board[move_index - 3])
        board[move_index - 1] = switch_value(board[move_index - 1])

    elif move_index == 4:
        board[1] = switch_value(board[1])
        board[5] = switch_value(board[5])
        board[3] = switch_value(board[3])
        board[7] = switch_value(board[7])

    return board


def switch_value(value):
    if value == 0:
        return 1
    else:
        return 0


def main():
    print('Welcome to this lights on lights off game.')
    print('You play on a 9x9 board. When you switch a light, the lights next to it are also switched.')
    print('Your goal is to turn all the lights off.')
    print('(1 is for a light on, 0 is for a light off.)')
    board = get_initial_board()

    while not is_board_winning(board):
        if loaded_q_table_list:
            print('Best move according to AI (Index):')
            values = loaded_q_table_list[sum(board)]
            index_of_max_value = values.index(max(values))
            print(values)
            print(index_of_max_value, 'with a score of', values[index_of_max_value])

        display_board(board)
        user_input = input("Enter your move: ")
        index = coordinate_to_index(user_input)
        board = update_board(board, index)


    print("Congratulations! You won!")


main()
