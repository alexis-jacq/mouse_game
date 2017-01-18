import matplotlib.pyplot as plt
import numpy as np
from mouse import Mouse


class Word:

    def __init__(self, n):
        u = np.linspace(0,5,n)
        v = np.linspace(0,5,n)
        x,y = np.meshgrid(u,v)
        x=np.sin((x+np.random.rand()*5)*np.pi)
        y=np.sin((y+np.random.rand()*5)*np.pi)
        self.grid = x+y
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
    score = 0
    N = 100
    word = Word(50)
    plt.imshow(word.grid, interpolation='nearest')
    plt.show()
    for trial in range(N):
        if trial%10==0:
            print trial
        word = Word(50)
        for i in range(word.n*word.n):
            word.update()
        #print word.energy
        score += word.energy
    print score/N
