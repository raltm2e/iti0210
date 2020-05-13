import random

import gym

"""        
        Observation:
        Type: Box(4)
        Num	Observation               Min             Max
        0	Cart Position             -4.8            4.8
        1	Cart Velocity             -Inf            Inf
        2	Pole Angle                -24 deg         24 deg
        3	Pole Velocity At Tip      -Inf            Inf
        
        Actions:
        Type: Discrete(2)
        Num	Action
        0	Push cart to the left
        1	Push cart to the right
"""

increment = 4
angle_increment = 10

def get_key(observation):
    cart_velocity = round(observation[1] * increment) / increment  # Grouping measurements by 0.2 increments
    pole_angle = round(observation[2] * angle_increment) / angle_increment
    returnable_tuple = (cart_velocity, pole_angle)
    return returnable_tuple


def get_best_move(q_table, observation):
    angle = round(observation[2] * angle_increment) / angle_increment
    for key in q_table:
        # If there is a key with this angle, get the key's velocity and return either 0 (left) or 1 (right)
        if key[1] == angle and q_table[key] > 1:
            if key[0] <= 0:
                return 0
            else:
                return 1
        else:
            return random.choice([0, 1])


def get_move(epsilon, q_table, observation):
    # Return either 0 (left) or 1 (right)
    if random.random() > epsilon:
        return get_best_move(q_table, observation)
    else:
        return random.choice([0, 1])


def main(learning_rate, gamma, epsilon):
    env = gym.make('CartPole-v0')
    q_table = {}

    for i_episode in range(200):
        observation = env.reset()
        for t in range(200):
            env.render()
            action = get_move(epsilon, q_table, observation)
            next_observation, reward, done, info = env.step(action)
            if done:
                reward = -reward  # simulatsioon lõppes enne 200 sammu, negatiivne tasu

            table_key = get_key(observation)  # Cart velocity and Pole angle
            next_table_key = get_key(next_observation)
            if table_key in q_table.keys():
                if next_table_key in q_table.keys():
                    q_table[table_key] += learning_rate * (reward + gamma * q_table[next_table_key] - q_table[table_key])
                else:
                    q_table[table_key] += learning_rate * reward
            else:
                q_table[table_key] = 0

            # Q[s,a] += learning_rate * (reward + gamma * Q[s',a'] - Q[s,a])

            observation = next_observation
            if done:
                print("Episode {} finished after {} timesteps".format(i_episode, t + 1))
                print(q_table)
                break
        if i_episode % 20 == 0 and epsilon > 0.1 and i_episode != 0:
            epsilon -= 0.1
    env.close()
    print(len(q_table.keys()))


if __name__ == '__main__':
    learning_rate = 0.1
    gamma = 1
    epsilon = 1  # Randomness chance when choosing an action
    main(learning_rate, gamma, epsilon)
