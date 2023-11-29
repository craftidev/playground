from environment import LightsGameEnvironment
from q_learning_agent import QLearningAgent
import numpy as np
import os

env = LightsGameEnvironment()
agent = QLearningAgent()
q_table_path = "q_table.npy"
success_number = 0

# Load the weights if exists
if os.path.exists(q_table_path):
    loaded_q_table = np.load(q_table_path)
    loaded_q_table_list = loaded_q_table.tolist()
    agent = QLearningAgent(
        q_table = loaded_q_table_list,
    )
    print('Q-table loaded')
else:
    agent = QLearningAgent()
    print('Starting a new Q-table')

# Loop for x episodes of n steps
for i in range(500_000):
    initial_state = env.reset()

    for _ in range(7):
        initial_action = agent.choose_action(initial_state)
        new_state, reward, done = env.step(initial_action)

        agent.update(
            initial_state,
            initial_action,
            reward,
            new_state
        )
        
        if done:
            success_number += 1
            break
    
    if i % 10_000 == 0:
        print(i, 'episodes')
        print(success_number / (i + 1), "success rate")
        print(agent.exploration_rate, 'was the exploration rate')

    # Exploration rate decay
    if agent.exploration_rate > 0.1:
        agent.exploration_rate -= agent.exploration_rate * 0.00001

# Save the weights
q_table = np.array(agent.q_table)
np.save(q_table_path, q_table)
print('Q-table saved')
