import sys
import pygame
from settings import Settings
from rocket import Rocket

class RocketGame:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Rocket Game')

        self.rocket = Rocket(self)



    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.rocket.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    rg = RocketGame()
    rg.run_game()