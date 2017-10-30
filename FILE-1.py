from pygame import *
from pygame.mixer import *
from pygame.sprite import *
import etc as b
import random

pygame.init()
active1 = True
active2 = True
moveup=False
movedown=False
moveright=False
obsmove=False

screen=display.set_mode((1080,800))
pygame.display.set_caption("ALIEN")

start=b.text_box("PRESS TO PLAY", 540, 350, 64)
help=b.text_box("Help",540,400,42)
all=Group(start, help)

ship=b.Alien()
obs=b.Obstace()
pic=Group(ship, obs)
while active1:
    screen.fill((255,255,255))
    all.draw(screen)
    display.update()

    for i in event.get():
        if i.type==QUIT:
            pygame.quit()
            exit()
            break

        elif i.type==MOUSEBUTTONUP:
            if start.rect.collidepoint(mouse.get_pos()):
                active = False
            while active2:
                screen.fill((255,255,255))
                pic.draw(screen)
                display.update()
                for main_event in event.get():

                    if main_event.type ==  KEYDOWN:
                        if main_event.key == K_UP:
                            moveup=True
                            obsmove=True
                        if main_event.key == K_DOWN:
                            movedown=True
                            obsmove=True
                        if main_event.key == K_RIGHT:
                            moveright=True
                            obsmove=True
                    if main_event.type ==  KEYUP:
                        if main_event.key == K_UP:
                            moveup=False
                        if main_event.key == K_DOWN:
                            movedown=False
                        if main_event.key == K_RIGHT:
                            moveright=False

                    if main_event.type == QUIT:
                        pygame.quit()
                        exit()
                    if ship.rect.colliderect(obs):
                        pygame.quit()
                        exit()

                if moveup == True:
                    ship.move(0, -1)

                if movedown == True:
                    ship.move(0, +1)
                if moveright == True:
                    ship.move(+1, 0)
                if obsmove==True:
                    obs.move(-1)
