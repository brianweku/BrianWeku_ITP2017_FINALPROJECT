#importing pygame, timer, music, random function, and other folder
from pygame import *
from pygame.sprite import *
import random
import burung_etc as b
import time

#start
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('pixel.mp3')
pygame.mixer.music.play(-1)


#screen resolution and its title of game
screen=display.set_mode((1080,800))
pygame.display.set_caption("BIRDOP")

#colors
black=(0,0,0)
white=(255,255,255)
brown=(160,82,45)




#sprites and pictures in the main menu
start=b.Sbutton()
inst=b.Hbutton()
bye=b.Ebutton()
menubg=image.load('bgground.png')
sound=b.Playbutton()
sound1=b.Pausebutton()
first=Group(start,inst,bye,sound,sound1)

#the main menu
def playon():
    active1 = True
    while active1:
        screen.fill(white)
        screen.blit(menubg, (0,0))
        first.draw(screen)
        display.update()

        for i in event.get():
            if i.type==QUIT:
                pygame.quit()
                exit()

            if i.type==KEYDOWN:
                if i.key==K_SPACE:
                    play()
                if i.key==K_ESCAPE:
                    pygame.quit()
                    exit()
            if i.type==MOUSEBUTTONDOWN:
                if bye.rect.collidepoint(mouse.get_pos()):
                    pygame.quit()
                    exit()
                if inst.rect.collidepoint(mouse.get_pos()):
                    help()
                if start.rect.collidepoint(mouse.get_pos()):
                    play()
                if sound1.rect.collidepoint(mouse.get_pos()):
                    pygame.mixer.music.pause()
                if sound.rect.collidepoint(mouse.get_pos()):
                    pygame.mixer.music.unpause()

#where the game starts
def play():
    #variables, classes
    score=0
    bird=b.Bird(100,350)
    pipeup=b.Pipeup()
    pipeup1=b.Pipeup1()
    pipedown=b.Pipedown()
    pipedown1=b.Pipedown1()
    bg1=b.Bg1(0)
    bg2=b.Bg2(1080)
    bg3=b.Bg3(2160)
    bg4=b.Bg4(3240)
    gover=image.load('gameover.png')
    flap=pygame.mixer.Sound('flap.ogg')
    point=pygame.mixer.Sound('point.ogg')
    crash=pygame.mixer.Sound('crash.ogg')
    active2 = True
    moveup=False
    movedown = False
    start_time=0
    postop=-500
    postbottom=1300
    posttop1=-700
    postbottom1=1100
    alientimer=0
    spawn=pygame.time.get_ticks()
    fourth=Group()
    fifth=(pipedown,pipeup,pipedown1,pipeup1)
    while active2:
        scoreboard=b.text_box("%d"%score, 540, 100, 35, white)
        second=Group(bg1, bg2, bg3, bg4, bird,pipedown,pipeup,pipedown1,pipeup1, scoreboard)
        screen.fill(white)

        second.draw(screen)
        fourth.draw(screen)
        display.update()
        for i in event.get():
            if i.type==QUIT:
                pygame.quit()
                exit()

            if i.type==KEYDOWN:
                if i.key==K_ESCAPE:
                        pygame.quit()
                        exit()
                if isinstance(bird, b.Bird):
                    if i.key==K_SPACE:
                        start_time=pygame.time.get_ticks()
                        moveup=True
                        flap.play()


                if isinstance(bird, b.Alien):
                    if i.key==K_UP:
                        moveup=True

                    if i.key==K_DOWN:
                        movedown=True



            if isinstance(bird,b.Alien):
                if i.type==KEYUP:
                    if i.key==K_UP:
                        moveup=False

                    if i.key==K_DOWN:
                        movedown=False

        if isinstance(bird,b.Alien):
            if moveup==True:
                bird.move(0,-3)


            if movedown==True:
                bird.move(0,3)


        if isinstance(bird,b.Bird):
            if pygame.time.get_ticks()-start_time>=500:
                moveup=False
                bird.normal()
            if pygame.time.get_ticks()-start_time>=700:
                moveup=False
                bird.down()
            if moveup==True:
                if bird.rect.top>=0:
                    bird.move(-5.5)
                    bird.up()
            if moveup==False:
                if bird.rect.bottom<=800:
                    bird.move(4)
        if pipeup.rect.right<=0:
            if pipedown.rect.bottom>=1350:
                newpos=random.randint(-125,0)
            elif pipeup.rect.top<=-200:
                newpos=random.randint(0,125)
            else:
                newpos=random.randint(-125,125)
            postop+=newpos
            postbottom+=newpos
            pipeup.nextpos(postop)
            pipedown.nextpos(postbottom)
            score+=1
            point.play()

        if pipeup1.rect.right<=0:
            if pipedown1.rect.bottom>=1350:
                newpos1=random.randint(-125,0)
            elif pipeup1.rect.top<=-200:
                newpos1=random.randint(0,125)
            else:
                newpos1=random.randint(-125,125)
            posttop1+=newpos1
            postbottom1+=newpos1
            pipeup1.nextpos(posttop1)
            pipedown1.nextpos(postbottom1)
            score+=1
            point.play()
        if bg1.rect.right<=0:
            bg1=b.Bg1(3240)
        if bg2.rect.right<=0:
            bg2=b.Bg2(3240)
        if bg3.rect.right<=0:
            bg3=b.Bg3(3240)
        if bg4.rect.right<=0:
            bg4=b.Bg4(3240)


        if bird.rect.colliderect(pipeup) or bird.rect.colliderect(pipedown) or bird.rect.colliderect(pipeup1) or bird.rect.colliderect(pipedown1):
            screen.fill(white)
            second.draw(screen)
            screen.blit(gover, (340, 300))
            display.update()
            crash.play()
            time.sleep(3)
            active2=False

        if spritecollideany(bird, fourth):
            alientimer=pygame.time.get_ticks()
            moveup=False
            bird = b.Alien(bird.rect.centerx,bird.rect.centery)



        if isinstance(bird,b.Alien):
            if pygame.time.get_ticks()-alientimer>=7000:
                bird=b.Bird(bird.rect.centerx,bird.rect.centery)
                movedown = False
                moveup = False
        if isinstance(bird, b.Bird):
            if pygame.time.get_ticks()-spawn>=17000:
                spawn=pygame.time.get_ticks()
                tempalien=b.Alien(1080,random.randint(300,500))
                fourth.add(tempalien)
        groupcollide(fifth,fourth,False,True)

        pipeup.move_left()
        pipedown.move_left()
        pipeup1.move_left()
        pipedown1.move_left()
        bg1.move_left()
        bg2.move_left()
        bg3.move_left()
        bg4.move_left()
        for alien in fourth:
            alien.move_left()

#picure in the help menu
direction=image.load('instructions.png')
back_button=b.Bbutton()
third=Group(back_button)

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

            if i.type==KEYDOWN:
                if i.key==K_ESCAPE:
                        pygame.quit()
                        exit()

            if i.type==MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(mouse.get_pos()):
                    active3=False


#PLAY
playon()


