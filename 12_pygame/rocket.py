import pygame

class Rocket:

    def __init__(self, rocket):
        self.screen = rocket.screen
        self.settings = rocket.settings
        self.screen_rect = rocket.screen.get_rect()

        self.image = pygame.image.load(
            'C:/Users/User/PycharmProjects/python_crash_course/aliens/images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

        #
        #     self.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)
