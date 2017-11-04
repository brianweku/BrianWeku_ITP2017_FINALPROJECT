from pygame import *
from pygame.mixer import *
from pygame.sprite import *
import random
import time
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



class text_box(Sprite):
    def __init__(self, message, x, y, font, color):
        Sprite.__init__(self)
        self.x=x
        self.y=y
        self.font=pygame.font.Font(None, font)
        self.image=self.font.render(message,1,black,color)
        self.rect=self.image.get_rect()
        self.rect.center=(x, y)

class Bbutton(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x=100
        self.y=700
        self.image=image.load('backbutton.png')
        self.rect=self.image.get_rect()
        self.rect.center=(self.x, self.y)

class Sbutton(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x=540
        self.y=370
        self.image=image.load('startbutton.png')
        self.rect=self.image.get_rect()
        self.rect.center=(self.x, self.y)

class Hbutton(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x=540
        self.y=450
        self.image=image.load('Helpbutton.png')
        self.rect=self.image.get_rect()
        self.rect.center=(self.x, self.y)
class Ebutton(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x=900
        self.y=700
        self.image=image.load('exitbutton.png')
        self.rect=self.image.get_rect()
        self.rect.center=(self.x, self.y)
class Alien(Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self)
        self.image=image.load('alien2.png')
        self.rect=self.image.get_rect()
        self.a=x
        self.b=y
        self.rect.center=((self.a, self.b))
    def move(self, a, b):
        self.a+=a
        self.b+=b
        self.rect.center=((self.a, self.b))
    def move_left(self):
        self.rect.left-=4


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

class Pipeup(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('pipeup.png')
        self.rect=self.image.get_rect()
        self.rect.top=-700
        self.rect.left=1000
    def move_left(self):
        self.rect.left-=4
    def nextpos(self, top):
        self.rect.left = 1080
        self.rect.top = top
class Pipedown(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('pipedown.png')
        self.rect=self.image.get_rect()
        self.rect.bottom=1500
        self.rect.left=1000
    def move_left(self):
        self.rect.left-=4
    def nextpos(self, bottom):
        self.rect.left = 1080
        self.rect.bottom = bottom



class Pipeup1(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('pipeup.png')
        self.rect=self.image.get_rect()
        self.rect.top=-500
        self.rect.left=1600
    def move_left(self):
        self.rect.left-=4
    def nextpos(self, top):
        self.rect.left = 1080
        self.rect.top = top
class Pipedown1(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('pipedown.png')
        self.rect=self.image.get_rect()
        self.rect.bottom=1300
        self.rect.left=1600
    def move_left(self):
        self.rect.left-=4
    def nextpos(self, bottom):
        self.rect.left = 1080
        self.rect.bottom = bottom

black=(0,0,0)
white=(255,255,255)
brown=(160,82,45)

