import gym
import pygame
pygame.init()
Surface = pygame.display.set_mode((600,600))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("RL")
env = gym.make('Acrobot-v1')

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            break
