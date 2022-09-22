import sys, pygame, random
from network import Network
from player import player
from ball import ball

pygame.init()

size = width, height = 1000, 600
black = 0, 0, 0
white = 255,255,255
speed = 2

win = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

def redrawWindow(win,player1,player2,ball):
    win.fill(black)
    player1.draw(win)
    player2.draw(win)
    ball.draw(win)
    pygame.display.update()

def main():
    n = Network()
    player1 = n.getPlayerp()

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        player2 = n.send(player1)
        for event in pygame.event.get(): 
             if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #game logic
        ball = n.getBallp()
        player1.move()
        #drawing
        redrawWindow(win,player1,player2,ball)

main()
