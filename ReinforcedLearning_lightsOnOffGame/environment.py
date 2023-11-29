import random

class LightsGameEnvironment:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.get_randomize_initial_board()
        self.done = False

    def get_randomize_initial_board(self):
        num_iterations = random.randint(1, 7)
        for _ in range(num_iterations):
            self.update_board(random.randint(0, 8))
        if self.is_board_winning():
            self.board = [0, 1, 0, 0, 1, 0, 0, 0, 0]
        self.board = [
            0, 1, 0,
            1, 1, 1,
            0, 1, 0
        ]

    def switch_value(self, value):
        return 1 if value == 0 else 0

    def is_board_winning(self):
        return sum(self.board) == 0

    def update_board(self, move_index):
        # Update logic similar to the provided code
        if move_index == -1:
            raise RuntimeError("Input move_index is invalid")

        self.board[move_index] = self.switch_value(self.board[move_index])

        # Define neighbors for each position on the board
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7]
        }

        for neighbor in neighbors[move_index]:
            self.board[neighbor] = self.switch_value(self.board[neighbor])

    def step(self, action):

        # Action is the index of the light to toggle
        self.update_board(action)

        reward = -1
        if self.is_board_winning():
            reward = 100
            self.done = True
        
        return self.board, reward, self.done

    def reset(self):
        # Reset the environment to a new random state
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.get_randomize_initial_board()
        self.done = False
        return self.board
