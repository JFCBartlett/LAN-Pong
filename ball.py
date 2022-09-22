import pygame, random

class ball:
    def __init__(self,x,y,width,height,colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x,y,width,height)
        self.velocity = [random.randint(4,8), random.randint(-8,8)]
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-8,8)