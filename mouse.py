import numpy as np

class Mouse:
    def __init__(self):
        pass

    def move(self,grid):
        return np.random.choice((-1,+1)),np.random.choice((-1,+1))

    def eat(self,reward):
        pass
