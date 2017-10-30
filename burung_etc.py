from pygame import *
from pygame.mixer import *
from pygame.sprite import *
import random
import time

class Bird(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('bird.png')
        self.rect=self.image.get_rect()
        self.a=100
        self.b=350
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
    def __init__(self, message, x, y, font):
        Sprite.__init__(self)
        self.x=x
        self.y=y
        self.font=pygame.font.Font(None, font)
        self.image=self.font.render(message,1,black,white)
        self.rect=self.image.get_rect()
        self.rect.center=(x, y)

class Alien(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('alien2.png')
        self.rect=self.image.get_rect()
        self.a=100
        self.b=350
        self.rect.center=((self.a, self.b))
    def move(self, a, b):
        self.a+=a
        self.b+=b
        self.rect.center=((self.a, self.b))

class Pipeup(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('pipeup.png')
        self.rect=self.image.get_rect()
        self.rect.top=-500
        self.rect.left=1000
    def move_left(self):
        self.rect.left-=3
    def nextpos(self, top):
        self.rect.left = 1000
        self.rect.top = top
class Pipedown(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('pipedown.png')
        self.rect=self.image.get_rect()
        self.rect.bottom=1300
        self.rect.left=1000
    def move_left(self):
        self.rect.left-=3
    def nextpos(self, bottom):
        self.rect.left = 1000
        self.rect.bottom = bottom



black=(0,0,0)
white=(255,255,255)

