import pygame

class icone(object):
    def __init__(self,link,largura,altura,posx,posy):
        self.image = pygame.image.load(link).convert_alpha()
        self.largura = largura
        self.altura = altura
        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        self.posx = posx
        self.posy = posy

