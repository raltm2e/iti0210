import gym

env = gym.make('CartPole-v0')

for i_episode in range(200):
    observation = env.reset()
    q_values = [[]]
    for t in range(200):
        env.render()

        # juhuslik action, selle asemel tee q-tabelist valimine epsilon-greedy põhimõttel
        action = env.action_space.sample()

        next_observation, reward, done, info = env.step(action)
        if done:
            reward = -reward   # simulatsioon lõppes enne 200 sammu, negatiivne tasu

        # treeni siin Q-tabelit
        learning_rate = 0.1
        gamma = 1
        #  Q[s,a] += learning_rate * (r + gamma * Q[s',a'] - Q[s,a])
        #  s: observation
        #  a: action
        #  r: reward
        #  s': next_observation
        #  a': parim action olekus s',
        #      pead ise leidma Q tabelist suurima väärtuse

        observation = next_observation
        if done:
            print("Episode {} finished after {} timesteps".format(i_episode, t+1))
            break
env.close()
