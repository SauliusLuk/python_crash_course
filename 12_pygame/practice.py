import sys
import pygame

class Bluewindow:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Blank Blue Window')

        self.bg_color = (176, 244, 230)

    def run_window(self):
        mario = Mario(self)  # Create a Mario instance
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            mario.blitme()  # Blit Mario onto the screen
            pygame.display.flip()

class Mario:
    def __init__(self, bluewindow):
        self.screen = bluewindow.screen
        self.screen_rect = bluewindow.screen.get_rect()

        self.image = pygame.image.load('image.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    window = Bluewindow()
    window.run_window()
