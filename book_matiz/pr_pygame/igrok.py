import pygame
class Igrok():
    def __init__(self,screen):
        self.screen=screen
        self.imege=pygame.image.load("imeges/igrok.bmp")
        self.rect=self.imege.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
    
    def blitme(self):
        self.screen.blit(self.imege,self.rect)
        