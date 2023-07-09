import pygame

class Rocket:

    def __init__(self, rocket):
        self.screen = rocket.screen
        self.screen_rect = rocket.screen.get_rect()

        self.image = pygame.image.load(
            'C:/Users/User/PycharmProjects/python_crash_course/aliens/images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
