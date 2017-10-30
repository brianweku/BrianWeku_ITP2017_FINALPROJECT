from pygame import *
from pygame.mixer import *
from pygame.sprite import *
import random
import burung_etc as b
import time


pygame.init()
mixer.init()
#music.load('')
#screen
screen=display.set_mode((1080,800))
pygame.display.set_caption("Hardcore Bird")

#colors
black=(0,0,0)
white=(255,255,255)

#

over=b.text_box('GAME OVER',540, 350, 50)

start=b.text_box("PRESS SPACE TO PLAY", 540, 350, 64)
inst=b.text_box('HELP', 540, 450, 64)
direction=image.load('instructions.png')
back_button=b.text_box('BACK ->', 100, 700, 64)

first=Group(start, inst)

third=Group(back_button)
#go
def menu():
    active1 = True
    while active1:
        screen.fill(white)
        first.draw(screen)
        display.update()

        for i in event.get():
            if i.type==QUIT:
                pygame.quit()
                exit()

            if i.type==KEYDOWN:
                if i.key==K_SPACE:
                    play()
            if i.type==MOUSEBUTTONDOWN:
                if inst.rect.collidepoint(mouse.get_pos()):
                    help()
def play():
    bird=b.Bird()
    pipeup=b.Pipeup()
    pipedown=b.Pipedown()
    second=Group(bird,pipedown,pipeup)
    active2 = True
    moveup=False
    start_time=0
    postop=-500
    postbottom=1300
    while active2:
        screen.fill(white)
        second.draw(screen)
        display.update()
        for i in event.get():
            if i.type==QUIT:
                pygame.quit()
                exit()

            if i.type==KEYDOWN:
                if i.key==K_SPACE:
                    start_time=pygame.time.get_ticks()
                    moveup=True
        if pygame.time.get_ticks()-start_time>=400:
            moveup=False
            bird.normal()
        if pygame.time.get_ticks()-start_time>=600:
            moveup=False
            bird.down()
        if moveup==True:
            if bird.rect.top>=0:
                bird.move(-2.5)
                bird.up()
        if moveup==False:
            if bird.rect.bottom<=800:
                bird.move(2)
        pipeup.move_left()
        pipedown.move_left()
        if pipeup.rect.right<=0:
            if pipeup.rect.top<=-400:
                newpos=random.randint(0,300)
            elif pipedown.rect.bottom>=1200:
                newpos=random.randint(-300,0)
            else:
                newpos=random.randint(-300,300)
            postop+=newpos
            postbottom+=newpos
            pipeup.nextpos(postop)
            pipedown.nextpos(postbottom)
        if bird.rect.colliderect(pipeup) or bird.rect.colliderect(pipedown):
            second.add(over)
            screen.fill(white)
            second.draw(screen)
            display.update()
            time.sleep(3)
            active2=False



def help():
    active3=True
    while active3:
        screen.blit(direction, (0,0))
        third.draw(screen)

        display.update()

        for i in event.get():
            if i.type==QUIT:
                pygame.quit()
                exit()

            if i.type==MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(mouse.get_pos()):
                    active3=False







menu()



