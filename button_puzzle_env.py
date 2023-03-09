import gymnasium as gym
from gymnasium import spaces
"import pygame"
import numpy as np

level_test_1 = np.ones((7,7))
level_test_1[1:6,1:6] = 0
level_test_1[4,2] = 3
level_test_1[5,5] = 4
level_test_1[3,4] = 5


class ButtonPuzzleEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self,render_mode = None) -> None:
        self.observation_space = spaces.Box(0,5,(7,7))
        self.action_space = spaces.Discrete(4)
        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

    def get_obs(self):
        return self.level
    
    def get_info(self):
        return {"player_x": self.player_x,"player_y": self.player_y}

    def reset(self):
        self.level = level_test_1
        self.player_x = 3
        self.player_y = 3

        observation = self.get_obs()

        #if self.render_mode == "human":
        #    self._render_frame()

        return observation, None
    
    def movement(self, y_move,x_move):
        moved_pos = self.level[self.player_y + y_move, self.player_x + x_move]
        next_pos = -1

        if moved_pos == 3:
            next_pos = self.level[self.player_y + 2*y_move, self.player_x + 2*x_move]
            if next_pos == 0:
                self.level[self.player_y + 2*y_move, self.player_x + 2*x_move] = 3
            elif next_pos == 4:
                self.terminated = True
            elif next_pos == 5:
                self.level[self.player_y + 2*y_move, self.player_x + 2*x_move] = 0

        if moved_pos == 0 or (moved_pos == 3 and next_pos in {0,5}):
            self.level[self.player_y,self.player_x] = 0
            self.player_y+=y_move
            self.player_x+=x_move
            self.level[self.player_y, self.player_x] = 2

    def step(self, action):
        self.terminated = False

        if action == 0: self.movement(-1,0)
        elif action == 1: self.movement(1,0)
        elif action == 2: self.movement(0,1)
        elif action == 3: self.movement(0,-1)

        reward = 1 if self.terminated else 0
        observation = self.get_obs()
        info = self.get_info()

        #if self.render_mode == "human":
        #    self._render_frame()

        return observation, reward, self.terminated, False, info