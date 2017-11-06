#importing pygame
from pygame import *
from pygame.sprite import *

#creating classes to be called on another file

#the bird
class Bird(Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self)
        self.image=image.load('bird.png')
        self.rect=self.image.get_rect()
        self.a=x
        self.b=y
        self.rect.center=((self.a, self.b))

    def move(self, b):
        self.b+=b
        self.rect.center=((self.a, self.b))

    def up(self):
        self.image=image.load('birdup.png')
        self.rect=self.image.get_rect()
        self.rect.center=((self.a, self.b))

    def normal(self):
        self.image=image.load('bird.png')
        self.rect=self.image.get_rect()
        self.rect.center=((self.a, self.b))

    def down(self):
        self.image=image.load('birddown.png')
        self.rect=self.image.get_rect()
        self.rect.center=((self.a, self.b))

#the alien icon and when it became one
class Alien(Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self)
        self.count=3
        self.image=image.load('images/alien3.png')

        self.rect=self.image.get_rect()
        self.a=x
        self.b=y
        self.rect.center=((self.a, self.b))
    def move(self, a, b):
        self.a+=a
        self.b+=b
        self.rect.center=((self.a, self.b))
    def move_left(self):
        self.rect.left-=4.5
    def Add(self):
        self.count += .25
    def checkcount(self):
        if self.count<=5:
            self.image=image.load('images/alien3.png')
        if self.count >= 5:
            self.image = image.load ('images/alien0.png')
        if self.count >= 10:
            self.image = image.load ('images/alien1.png')

        if self.count >=15:
            self.count=0

#if i want to add a text box button
class text_box(Sprite):
    def __init__(self, message, x, y, font, color):
        Sprite.__init__(self)
        self.x=x
        self.y=y
        self.font=pygame.font.Font(None, font)
        self.image=self.font.render(message,1,black,color)
        self.rect=self.image.get_rect()
        self.rect.center=(x, y)
#play music button
class Playbutton(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x=100
        self.y=100
        self.image=image.load('play.png')
        self.rect=self.image.get_rect()
        self.rect.center=(self.x, self.y)
#pause mmusic button
class Pausebutton(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x=155
        self.y=100
        self.image=image.load('pause.png')
        self.rect=self.image.get_rect()
        self.rect.center=(self.x, self.y)
#back button
class Bbutton(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x=100
        self.y=700
        self.image=image.load('backbutton.png')
        self.rect=self.image.get_rect()
        self.rect.center=(self.x, self.y)
#start button
class Sbutton(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x=540
        self.y=370
        self.image=image.load('startbutton.png')
        self.rect=self.image.get_rect()
        self.rect.center=(self.x, self.y)
#help button
class Hbutton(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x=540
        self.y=450
        self.image=image.load('Helpbutton.png')
        self.rect=self.image.get_rect()
        self.rect.center=(self.x, self.y)
#exit button
class Ebutton(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x=900
        self.y=700
        self.image=image.load('exitbutton.png')
        self.rect=self.image.get_rect()
        self.rect.center=(self.x, self.y)

#moving backgrounds
class Bg1(Sprite):
    def __init__(self, x):
        Sprite.__init__(self)
        self.image=image.load('gamebg1.png')
        self.rect=self.image.get_rect()
        self.x=x
        self.rect.top=0
        self.rect.left=x
    def move_left(self):
        self.rect.left-=4
class Bg2(Sprite):
    def __init__(self,x):
        Sprite.__init__(self)
        self.image=image.load('gamebg2.png')
        self.rect=self.image.get_rect()
        self.x=x
        self.rect.top=0
        self.rect.left=x
    def move_left(self):
        self.rect.left-=4
class Bg3(Sprite):
    def __init__(self, x):
        Sprite.__init__(self)
        self.image=image.load('gamebg3.png')
        self.rect=self.image.get_rect()
        self.x=x
        self.rect.top=0
        self.rect.left=x
    def move_left(self):
        self.rect.left-=4
class Bg4(Sprite):
    def __init__(self, x):
        Sprite.__init__(self)
        self.image=image.load('gamebg4.png')
        self.rect=self.image.get_rect()
        self.x=x
        self.rect.top=0
        self.rect.left=x
    def move_left(self):
        self.rect.left-=4


class Pipeup(Sprite):#first pair of pipes
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('pipeup.png')
        self.rect=self.image.get_rect()
        self.rect.top=-700
        self.rect.left=1000
    def move_left(self):
        self.rect.left-=4.5
    def nextpos(self, top):
        self.rect.left = 1080
        self.rect.top = top
class Pipedown(Sprite): #first pair of pipes
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('pipedown.png')
        self.rect=self.image.get_rect()
        self.rect.bottom=1500
        self.rect.left=1000
    def move_left(self):
        self.rect.left-=4.5
    def nextpos(self, bottom):
        self.rect.left = 1080
        self.rect.bottom = bottom

class Pipeup1(Sprite): #second pair of pipes
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('pipeup.png')
        self.rect=self.image.get_rect()
        self.rect.top=-500
        self.rect.left=1600
    def move_left(self):
        self.rect.left-=4.5
    def nextpos(self, top):
        self.rect.left = 1080
        self.rect.top = top
class Pipedown1(Sprite): #second pair of pipes
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('pipedown.png')
        self.rect=self.image.get_rect()
        self.rect.bottom=1300
        self.rect.left=1600
    def move_left(self):
        self.rect.left-=4.5
    def nextpos(self, bottom):
        self.rect.left = 1080
        self.rect.bottom = bottom

#color RGB code
black=(0,0,0)
white=(255,255,255)
brown=(160,82,45)

 