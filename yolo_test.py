import gym
import numpy as np

# Initialize the environment
env = gym.make('Taxi-v3')

# Define Q-Learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
q_table = np.zeros((env.observation_space.n, env.action_space.n))
# Initialize the environment
env = gym.make('Taxi-v3')

# Define Q-Learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
epsilon_min = 0.01  # Minimum exploration rate
epsilon_decay = 0.99  # Exploration rate decay
q_table = np.zeros((env.observation_space.n, env.action_space.n))

def q_learning(env, q_table, alpha, gamma, epsilon, epsilon_min, epsilon_decay, episodes=10000):
    for episode in range(episodes):
        state = env.reset()  # Ensure state is an integer
        done = False
        rewards = 0.0

        if np.random.rand() < epsilon:
            action = np.random.choice(env.action_space.n)
        else:
            if state < 0 or state >= q_table.shape[0]:
                raise IndexError(f"Invalid state index: {state}")
            action = np.argmax(q_table[state])  # Ensure valid state index

            next_state, reward, done, _ = env.step(action)
            rewards += reward

            # Q-Learning update rule
            q_table[state, action] = (1 - alpha) * q_table[state, action] + alpha * (reward + gamma * np.max(q_table[next_state]))

            state = next_state

        if episode % 100 == 0:
            print(f'Episode {episode}, Reward: {rewards}')

        # Decay exploration rate
        epsilon = max(epsilon_min, epsilon * epsilon_decay)

    return q_table

def test_agent(env, q_table, episodes=100):
    rewards = 0.0
    for episode in range(episodes):
        state = env.reset()
        done = False
        episode_rewards = 0.0

        while not done:
            action = np.argmax(q_table[state])
            next_state, reward, done, _ = env.step(action)
            episode_rewards += reward
            state = next_state

        rewards += episode_rewards

    average_reward = rewards / episodes
    print(f'Average Reward over {episodes} episodes: {average_reward}')

# Train the Q-Learning model
trained_q_table = q_learning(env, q_table, alpha, gamma, epsilon, epsilon_min, epsilon_decay, episodes=10000)
# Test the trained agent
test_agent(env, trained_q_table)
def q_learning(env, q_table, alpha, gamma, epsilon, episodes=10000):
    for episode in range(episodes):
        state = env.reset()
        done = False
        rewards = 0.0

    while not done:
        if np.random.rand() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])

    next_state, reward, done, _ = env.step(action)
    rewards += reward

    # Q-Learning update rule
    q_table[state, action] = (1 - alpha) * q_table[state, action] + alpha * (reward + gamma * np.max(q_table[next_state]))

    state = next_state

            # Q-Learning update rule
    q_table[state, action] = (1 - alpha) * q_table[state, action] + alpha * (reward + gamma * np.max(q_table[next_state]))

    state = next_state

    if episode % 100 == 0:
            print(f'Episode {episode}, Reward: {rewards}')

    return q_table

def test_agent(env, q_table, episodes=100):
    rewards = 0.0
    for episode in range(episodes):
        state = env.reset()
        done = False
        episode_rewards = 0.0

        while not done:
            action = np.argmax(q_table[state])
            next_state, reward, done, _ = env.step(action)
            episode_rewards += reward
            state = next_state

        rewards += episode_rewards

    average_reward = rewards / episodes
    print(f'Average Reward over {episodes} episodes: {average_reward}')

# Train the Q-Learning model
trained_q_table = q_learning(env, q_table, alpha, gamma, epsilon)

# Test the trained agent
test_agent(env, trained_q_table)

