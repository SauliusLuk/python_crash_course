import sys
import pygame
from pygame.locals import *

class EmptyScreen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('Empty screen')
        self.bg_color = (110, 230, 230)
        self.font = pygame.font.Font(None, 24)
        self.message = ""

    def run_screen(self):
        while True:
            self._check_events()
            self.screen.fill(self.bg_color)
            self._blit_message()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.message = f"Key '{pygame.key.name(event.key)}' pressed"

    def _blit_message(self):
        text_surface = self.font.render(self.message, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
        self.screen.blit(text_surface, text_rect)

if __name__ == '__main__':
    es = EmptyScreen()
    es.run_screen()



