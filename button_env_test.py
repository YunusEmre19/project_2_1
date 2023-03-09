import gymnasium as gym
from button_puzzle_env import ButtonPuzzleEnv
import os
import time
env = ButtonPuzzleEnv(render_mode="human")
observation, info = env.reset()
for i in range(30):

    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    os.system("cls")
    print(observation)
    time.sleep(1)

    if terminated or truncated:
        observation, info = env.reset()

env.close()