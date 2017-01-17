import numpy as np
from mouse import Mouse

class Word:

    def __init__(self, n):
        self.grid = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                self.grid[i,j] = 1-2*np.random.rand()
        self.n = n
        self.x = 0; self.y = 0
        self.mouse = Mouse()
        self.energy = 0

    def vew(self):
        out = np.zeros((self.n,self.n))
        out[0:self.n-self.x,0:self.n-self.y] = self.grid[self.x:self.n,self.y:self.n]
        out[self.n-self.x:self.n,self.n-self.y:self.n] = self.grid[0:self.x,0:self.y]
        out[self.n-self.x:self.n,0:self.n-self.y] = self.grid[0:self.x,self.y:self.n]
        out[0:self.n-self.x,self.n-self.y:self.n] = self.grid[self.x:self.n,0:self.y]
        return out

    def update(self):
        dx,dy = self.mouse.move(self.vew())
        self.x=(self.x+dx)%self.n; self.y=(self.y+dy)%self.n
        self.mouse.eat(self.grid[self.x,self.y])
        self.energy += self.grid[self.x,self.y]
        self.grid[self.x,self.y] = 0

if __name__=="__main__":
    word = Word(10)
    for i in range(word.n*word.n*10):
        word.update()
    print word.energy
