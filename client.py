import pygame
import sys
from network import Network

pygame.init()

size = width, height = 1000, 600
black = 0, 0, 0
white = 255, 255, 255
speed = 2

win = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")


def redrawWindow(window, player1, player2, ball):
    win.fill(black)
    player1.draw(window)
    player2.draw(window)
    ball.draw(window)
    pygame.display.update()


def main():
    n = Network()
    player1 = n.getPlayerp()
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        player2 = n.sendPlayer(player1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # game logic
        ball = n.getBallp()
        player1.move()
        # drawing
        redrawWindow(win, player1, player2, ball)


main()
