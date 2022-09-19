import pygame

class player:
    def __init__(self,x,y,width,height,colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x,y,width,height)

    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)
    def move(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.y -= 5
            if self.y < 0:
                self.y = 0
        if keystate[pygame.K_DOWN]:
            self.y += 5
            if self.y > 440:
                self.y = 440

        self.rect = (self.x,self.y,self.width,self.height)