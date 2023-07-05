import pygame
class Mario:
    def __init__(self, bluewindow):
        self.screen = bluewindow.screen
        self.screen_rect = bluewindow.screen.get_rect()

        self.image = pygame.image.load('image.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)