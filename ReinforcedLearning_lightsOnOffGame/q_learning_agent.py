import random

# :params q_table: to import a Q-value table.
class QLearningAgent:
    def __init__(
        self,
        action_space = 9,       # 9 possible action on a 3x3 board.
        learning_rate = 1,    # How much of the new estimate we adopt.
        discount_factor = 0.8,  # 0 short-sighted, 1 long-term rewards.
        exploration_rate = 0.1, # chance of deviation (decay in main)
        q_table = None
    ):
        # Number of actions
        self.action_space = action_space
        self.q_table = q_table

        # Q-table scores initialization.
        # Create a matrice of all 2^9 = 512 possible states of 3x3.
        if self.q_table is None:
            self.q_table = [[0 for _ in range(self.action_space)] for _ in range(2 ** 9)]
            self.q_table[0] = [100] * self.action_space

        # Learning parameters
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

    def choose_action(self, state):
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(range(self.action_space))
        else:
            state_index = self.state_to_index(state)
            return self.q_table[state_index].index(
                    max(self.q_table[state_index])
            )

    def state_to_index(self, state):
        # Convert the binary representation of the board to an integer
        return int(''.join(map(str, state)), 2)

    def update(self, state, action, reward, next_state):
        state_index = self.state_to_index(state)
        next_state_index = self.state_to_index(next_state)

        # Q-learning update rule
        best_next_action = \
            self.q_table[next_state_index].index(
                max(self.q_table[next_state_index])
            )

        self.q_table[state_index][action] += \
            self.learning_rate * (
                reward +
                self.discount_factor *
                self.q_table[next_state_index][best_next_action] -
                self.q_table[state_index][action]
            )
