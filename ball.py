import pygame
import random


class ball:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (self.x, self.y, width, height)
        self.velocity = [random.randint(4, 8), random.randint(-8, 8)]

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        if self.y < 0:
            self.velocity[1] = -self.velocity[1]
        elif self.y > 580:
            self.velocity[1] = -self.velocity[1]
        if self.x < 0:
            self.x = 400
            self.y = 300
            self.velocity[0] = random.randint(4, 8)
        elif self.x > 980:
            self.x = 400
            self.y = 300
            self.velocity[0] = random.randint(4, 8)
        self.rect = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-8, 8)
