import pygame
from network import Network
from player import Player

width, height = 500, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

def read_pos(str):
    str = str.split(",")
    return int(str[0]),int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(win, player1, player2):
    win.fill((255, 255, 255))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    startpos = read_pos(n.getpos())
    p1 = Player(startpos[0], startpos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 0, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2pos = read_pos(n.send(make_pos((p1.x, p1.y))))
        p2.x = p2pos[0]
        p2.y = p2pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p1.move()
        redrawWindow(win, p1, p2)

main()