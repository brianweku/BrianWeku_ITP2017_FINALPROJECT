from pygame import *
from pygame.mixer import *
from pygame.sprite import *
import random

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

class Obstace(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=image.load('crate.png')
        self.rect=self.image.get_rect()
        self.a=1050
        self.b=0
        self.rect.top=(self.b)
        self.rect.right=(self.a)
    def move(self, a):
        self.a+=a
        self.rect.right=((self.a))
black=(0,0,0)
white=(255,255,255)
