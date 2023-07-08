import sys
import pygame
from game_character import Mario

class Bluewindow:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Blank Blue Window')
        self.mario = Mario(self)
        self.bg_color = (250, 250, 250)

    def run_window(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.mario.blitme()
            pygame.display.flip()
    def blitme(self):
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    window = Bluewindow()
    window.run_window()