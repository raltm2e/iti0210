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


def get_best_move(q_table):
    biggest_value = -999999
    correct_key = ()
    for key in q_table:
        if q_table[key] > biggest_value:
            biggest_value = q_table[key]
            correct_key = key
    if len(correct_key) == 0:
        return random.choice([0, 1])
    # if cart is going left
    if correct_key[0] < 0:
        return 0
    else:
        return 1


def get_move(epsilon, q_table):
    # Return either 0 (left) or 1 (right)
    if random.random() > epsilon:
        return get_best_move(q_table)
    else:
        return random.choice([0, 1])


def main(learning_rate, gamma, epsilon):
    env = gym.make('CartPole-v0')
    q_table = {}

    for i_episode in range(200):
        observation = env.reset()
        for t in range(200):
            env.render()
            action = get_move(epsilon, q_table)

            next_observation, reward, done, info = env.step(action)
            if done:
                reward = -reward  # simulatsioon lõppes enne 200 sammu, negatiivne tasu

            cart_velocity = round(observation[1], 1)
            if cart_velocity == -0.0:
                cart_velocity = 0.0
            table_key = (cart_velocity, round(observation[2], 1))  # Cart velocity and Pole angle
            next_cart_velocity = round(next_observation[1], 1)
            if next_cart_velocity == -0.0:
                next_cart_velocity = 0.0
            next_table_key = (next_cart_velocity, round(next_observation[2], 1))

            if table_key in q_table.keys():
                if next_table_key in q_table.keys():
                    q_table[table_key] += learning_rate * (reward + gamma * q_table[next_table_key] - q_table[table_key])
                else:
                    q_table[table_key] += learning_rate * reward
            else:
                q_table[table_key] = learning_rate * reward

            # Q[s,a] += learning_rate * (reward + gamma * Q[s',a'] - Q[s,a])

            observation = next_observation
            if done:
                print("Episode {} finished after {} timesteps".format(i_episode, t + 1))
                print(q_table)
                break
        if i_episode % 50 == 0 and epsilon > 0.1 and i_episode != 0:
            epsilon -= 0.1
    env.close()
    print(len(q_table.keys()))


if __name__ == '__main__':
    learning_rate = 0.1
    gamma = 1
    epsilon = 1  # Randomness chance when choosing an action
    main(learning_rate, gamma, epsilon)
